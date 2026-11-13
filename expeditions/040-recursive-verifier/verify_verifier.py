"""Generate fixed signed clause templates and attack the physical verifier at all seeds."""
import argparse
import json
import random

import recursive_rs as rs
import verify_geometry as ref
from clause_compiler import BitCircuit, FULL, PhysicalCNF, SEEDS, require, signed


def direct(a, cells, no, detached=None):
    """Scalar clause residual and separate leaf interpolation on absolute points."""
    if not ref.degree_below(tuple(SEEDS), a, 2):
        return 0
    rows = []
    for v, points in enumerate(ref.ROWS):
        word = [cells[(w // 8) * 128 + v * 8 + w % 8] for w in range(64)]
        if detached == "parent":
            word[:8] = [0] * 8
        rows.append(ref.degree_below(points, word, 8))
    cols = []
    for c in range(32):
        word = [cells[(4 + c // 8) * 128 + v * 8 + c % 8] for v in range(16)]
        if detached == "column":
            word = [0] * 16
        cols.append(ref.degree_below(ref.COLUMNS, word, 2))
    passed = 0
    for x in SEEDS:
        if not rows[x >> 3] or not all(cols[(x & 7) + 8 * f] for f in range(4)):
            continue
        first = ref.product([x ^ t for t in (1, 2, 3)] +
                            [a[x] ^ 1, a[x] ^ 1, a[x ^ int(not no)] ^ 1])
        second = ref.product([x ^ t for t in (0, 2, 3)] + [a[x ^ int(no)]] * 3)
        range_check = ref.product([x, x ^ 1, a[x ^ 2], a[x ^ 2] ^ 1])
        quotient = ref.product([x ^ t for t in (0, 1, 2, 3)] + [cells[x]])
        if first ^ second ^ range_check ^ quotient == 0:
            passed |= 1 << x
    return passed


def sharp_cells():
    coeffs = rs.vanishing(range(4, 20))
    scale = rs.inv(coeffs[0])
    quotient = [rs.mul(c, scale) for c in coeffs[1:]]
    cells = rs.honest_cells(quotient)
    require(all(ref.mul(x, cells[x]) == 1 for x in range(4, 20)), "sharp quotient")
    return cells


def cases():
    linear = [x ^ 1 for x in SEEDS]
    zero = [0] * 128
    honest = rs.honest_cells([0, 1])
    sharp = sharp_cells()
    perturbed = sharp.copy()
    perturbed[24] ^= 1
    recip = [0] + [ref.inverse(x) for x in range(1, 128)]
    fixtures = {
        "perfect_yes": (linear, honest), "sharp_no": (zero, sharp),
        "sharp_no_noncode": (zero, perturbed),
        "inverse_zero_extension": (zero, recip + [0] * 896),
        "inverse_interpolated_rows": (zero, ref.extend_rows(recip)),
    }
    # Mutate one physical word in every row in each of the eight pages.
    # Mutations include the high symbol bits of each extension page.
    for page in range(8):
        for row in range(16):
            word = 128 * page + 8 * row + ((page + row) % 8)
            changed = honest.copy()
            changed[word] ^= 1 << ((row + page) % (7 if page == 0 else 14))
            fixtures[f"single_{page}_{row}"] = linear, changed
    rng = random.Random(40128)
    for i in range(8):
        coeffs = [rng.randrange(128) for _ in range(16)]
        fixtures[f"code_{i}"] = linear, rs.honest_cells(coeffs)
    bad_a = linear.copy()
    bad_a[17] ^= 1
    fixtures["broken_affine_A"] = bad_a, honest
    return fixtures


def check_pin_addresses(layout):
    for z in SEEDS:
        for i, wire in enumerate(layout.circuit.public):
            for bit in (0, 1):
                clamped = (z & ~(1 << i)) | (bit << i)
                literal = layout.address(wire if bit else -wire, clamped)
                require(((abs(literal) - 1) & 127) == clamped and (literal > 0) == bool(bit),
                        "bad public pin projection")


def run():
    fixtures = cases()
    results = {}
    for no in (False, True):
        circuit = BitCircuit().compile(no)
        layout = PhysicalCNF(circuit)
        check_pin_addresses(layout)
        named = {}
        for name, (a, cells) in fixtures.items():
            vals = circuit.evaluate(a, cells)
            table = signed(vals, circuit.output)
            expected = direct(a, cells, no)
            require(table == expected, f"field and Boolean verdicts differ: {name}, NO={no}")
            if name.startswith(("single_", "code_")):
                continue
            rejected = 128 - table.bit_count()
            physical = layout.pack_assignment(vals)
            require(layout.failures(physical) == rejected, "physical CNF failed-pair count")
            named[name] = rejected
            if (not no and name == "perfect_yes") or (no and name.startswith("sharp_no")):
                correct = 0 if not no else 109
                require(rejected == correct, "sharp witness count")
                if no:
                    require(table == sum(1 << t for t in range(1, 20)), "wrong residual roots")
                # Flip the final gate at one addressed seed: the gate relation
                # detects the dishonest output even when it heals its unit clause.
                wire = abs(circuit.output)
                tag, _ = layout.read[wire]
                physical[tag] ^= 1
                require(layout.failures(physical) >= correct, "verdict can evade gate clauses")
                physical[tag] ^= 1
                if not no:
                    for w in circuit.public:
                        tag, _ = layout.read[w]
                        physical[tag] ^= 1
                        require(layout.failures(physical) >= 2, "clamped public seed escaped")
                        physical[tag] ^= 1
        results["no" if no else "yes"] = {
            "binary_gates": len(circuit.gates), "physical_variables": 128 * layout.num_tags,
            "templates_including_pins": layout.template_count,
            "clause_seed_pairs": 128 * layout.template_count,
            "global_pairs_compared": len(fixtures), "seeds_each": 128,
            "canonical_failed_pairs": named}
    split = {}
    for attack, key in (("parent", "inverse_zero_extension"),
                        ("column", "inverse_interpolated_rows")):
        a, cells = fixtures[key]
        joined = direct(a, cells, True)
        broken = direct(a, cells, True, detached=attack)
        require(joined == 0 and broken == FULL ^ 1, "alias-splitting counterexample")
        split[attack] = {"joined_accept": joined.bit_count(), "detached_accept": broken.bit_count()}
    results["false_layouts"] = split
    # Use independent field arithmetic and the wrong row's interpolation basis.
    honest = rs.honest_cells([0, 1])
    roots = [honest[8 + u] for u in range(8)]
    wrong = ref.interpolate(ref.ROWS[0][:8], roots, ref.ROWS[0][32])
    correct = honest[rs.row_cell(1, 32)]
    require((correct, wrong) == (384, 392), "incorrect-weight counterexample")
    results["row_1_slot_32"] = {"honest": correct, "using_row_0_weights": wrong}
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dimacs", choices=("yes", "no"), help="export all clauses, with multiplicities")
    parser.add_argument("--assignment", choices=("yes", "no"), help="export the extremal physical witness, one byte per variable")
    args = parser.parse_args()
    if args.dimacs and args.assignment:
        parser.error("choose one export")
    if args.dimacs or args.assignment:
        import sys
        no = (args.dimacs or args.assignment) == "no"
        circuit = BitCircuit().compile(no)
        layout = PhysicalCNF(circuit)
        if args.assignment:
            a = [0] * 128 if no else [x ^ 1 for x in SEEDS]
            cells = sharp_cells() if no else rs.honest_cells([0, 1])
            proof = layout.pack_assignment(circuit.evaluate(a, cells))
            sys.stdout.buffer.write(bytes((word >> z) & 1 for word in proof for z in SEEDS))
            return
        print("p cnf", layout.num_tags * 128, layout.template_count * 128)
        for z in SEEDS:
            for clause in layout.clauses_at(z):
                print(*clause, 0)
        return
    print(json.dumps(run(), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
