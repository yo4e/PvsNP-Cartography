"""Exact finite cost, semantics, and unrestricted signed-error checks.

No finite witness set here supplies a universal NO lower bound. The all-error
upper bound uses the inherited local gate charge; actual singleton witnesses
give the matching lower bound where reported.
"""
import hashlib
import json
import random

from sparse_compiler import (DIRECTIONS, OFFSETS, SparseCircuit, affine_bad_seeds,
                             build, cc, direct, fanout, inherited, offsets_for, ref, rs)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def extra_fixtures():
    yes_a = [x ^ 1 for x in range(128)]
    yes_cells = rs.honest_cells([0, 1])
    sharp = inherited.sharp_cells()
    out = {}
    # Single physical A-bit errors cover every seed and every symbol bit in
    # the membership-only control below. Full scalar/Boolean comparisons
    # retain representative points, axes, and polynomial/nonpolynomial words.
    for p, bit in ((0, 0), (1, 6), (2, 3), (17, 0), (63, 4), (127, 6)):
        a = yes_a.copy()
        a[p] ^= 1 << bit
        out[f"A_single_{p}_{bit}"] = a, yes_cells
    for j in range(7):
        a = [x ^ 1 ^ ((x >> j) & 1) for x in range(128)]
        out[f"A_additive_nonfield_{j}"] = a, yes_cells
    out["A_square"] = [ref.mul(x, x) for x in range(128)], sharp
    rng = random.Random(45128)
    for count in (2, 7, 31, 64, 128):
        a = [0] * 128
        for p in rng.sample(range(128), count):
            a[p] = rng.randrange(1, 128)
        out[f"A_random_{count}"] = a, sharp
    # A splice tests nonuniform slopes without changing the shared B table.
    out["A_half_splice"] = [0 if x < 64 else x ^ 1 for x in range(128)], sharp
    a = [0] * 128
    for s in OFFSETS:
        point = 96 ^ s
        a[point] = ref.mul(100, point)
    out["A_star_splice_NO108"] = a, sharp
    a = [0] * 128
    for center, slope in ((96, 100), (117, 92), (122, 98)):
        for s in OFFSETS:
            point = center ^ s
            a[point] = ref.mul(slope, point)
    out["A_three_stars_NO106"] = a, sharp
    # Explicit radius-two attack supplied by the sibling skeptic. It is
    # checked here through independent scalar field arithmetic and the full
    # Boolean compiler, without importing that agent's attack evaluator.
    a = [ref.mul(121, x) ^ 1 if (x ^ 124).bit_count() <= 2 else 0
         for x in range(128)]
    coefficients = [55, 43, 75, 65, 76, 75, 115, 57, 19, 48, 29, 73, 27, 2, 26, 95]
    out["A_radius2_splice_NO108"] = a, rs.honest_cells(coefficients)
    return out


def membership_controls(radius):
    checks = 0
    a = [x ^ 1 for x in range(128)]
    for p in range(128):
        for bit in range(7):
            changed = a.copy()
            changed[p] ^= 1 << bit
            bad = affine_bad_seeds(changed, radius)
            require(set(bad) == {p ^ s for s in offsets_for(radius)}, "single-symbol star support")
            checks += 1
    return {"single_bit_membership_cases": checks,
            "bad_seeds_each": len(offsets_for(radius)), "offsets": list(offsets_for(radius))}


def map_control(circuit, layout):
    by_tag = {}
    for key, wire in circuit.inputs.items():
        if key[0] not in ("A", "B"):
            continue
        tag, delta = layout.read[wire]
        require(delta == key[3], "fixed XOR offset preserved")
        by_tag.setdefault((key[0], key[1], key[2], tag), set()).add(delta)
    maximum = {}
    for (role, page, bit, tag), offsets in by_tag.items():
        maximum[role] = max(maximum.get(role, 0), len(offsets))
        if role == "A":
            require(offsets == set(circuit.source.offsets), "exact A maps")
    require(maximum == {"A": len(circuit.source.offsets), "B": 23}, "physical reader census")
    # Two wire keys name the same physical bit iff their tag and XOR point
    # agree. The layout is explicit; don't detach aliases for row/column reads.
    original = cc.PhysicalCNF(circuit.source)
    require(all(layout.read[w] == original.read[w] for w in circuit.physical),
            "private-copy transformation preserves physical aliases")
    inherited.check_pin_addresses(layout)
    return maximum


def check_radius(radius, caps):
    selected_cap = {1: 21, 2: 27, "cross": 21}[radius]
    sigma = max(23, len(offsets_for(radius)))
    result = {"schedule": radius, "membership_controls": membership_controls(radius), "layouts": {}}
    extra = extra_fixtures()
    fixtures = inherited.cases() | extra
    verdicts = {}
    for no in (False, True):
        source = SparseCircuit(radius).compile(no)
        details = {}
        digest = hashlib.sha256()
        for name, (a, cells) in fixtures.items():
            scalar = direct(a, cells, no, radius)
            values = source.evaluate(a, cells)
            packed = cc.signed(values, source.output)
            require(scalar == packed, f"scalar/Boolean mismatch {name}, no={no}")
            verdicts[no, name] = scalar
            digest.update(name.encode() + b"\0" + scalar.to_bytes(16, "little"))
            if not name.startswith(("single_", "code_")):
                details[name] = 128 - scalar.bit_count()
        result["no" if no else "yes"] = {
            "field_assignments_compared": len(fixtures), "seeds_each": 128,
            "verdict_stream_sha256": digest.hexdigest(), "named_rejections": details}
    if radius in (1, 2):
        require(result["no"]["named_rejections"]["A_star_splice_NO108"] == (108 if radius == 1 else 114),
                "independent star-splice counterexample replay")
    if radius == 2:
        require(result["no"]["named_rejections"]["A_radius2_splice_NO108"] == 108,
                "radius-two splice counterexample replay")
    if radius == 1:
        require(result["no"]["named_rejections"]["A_three_stars_NO106"] == 106,
                "three-star splice counterexample replay")
    if radius == "cross":
        require(all(result["no"]["named_rejections"][name] >= 109 for name in
                    ("A_star_splice_NO108", "A_radius2_splice_NO108", "A_three_stars_NO106")),
                "cross schedule rejects all splices at least109 times")
    yes_a, yes_cells = fixtures["perfect_yes"]
    # f=21 is the largest cap that leaves the physical B load 23 dominant.
    # Neighboring caps and f=2 check the actual padding/cap tradeoff, not a
    # claimed optimization over all possible compilers.
    for cap in caps:
        summary = {}
        for no in (False, True):
            circuit, layout = build(no, cap, radius)
            readers = map_control(circuit, layout)
            named_a, named_cells = fixtures["sharp_no" if no else "perfect_yes"]
            values = circuit.evaluate(named_a, named_cells)
            proof = layout.pack_assignment(values)
            expected = 109 if no else 0
            require(layout.failures(proof) == expected, "canonical witness failed pairs")
            d = fanout.census(circuit, layout) | {
                "copy_rows": circuit.copy_count, "physical_reader_maxima": readers,
                "canonical_witness_failed_pairs": expected}
            if cap == selected_cap:
                # Compare transformed semantics for every previously checked
                # field assignment, and evaluate full physical clauses on
                # every named new noncode assignment.
                for name, (a, cells) in fixtures.items():
                    vals = circuit.evaluate(a, cells)
                    require(cc.signed(vals, circuit.output) == verdicts[no, name],
                            "private-copy verdict mismatch")
                    if name in extra or name.startswith("sharp_no"):
                        require(layout.failures(layout.pack_assignment(vals)) ==
                                128-verdicts[no, name].bit_count(), "truthful full physical CNF")
                d["private_copy_assignments_compared"] = len(fixtures)
            if not no:
                bound = fanout.uniform_signed_bound(circuit, layout)
                d["signed_upper_bound"] = bound
                if cap in (2, selected_cap):
                    singletons, loads = fanout.singleton_loads(cc, circuit, layout, values)
                    require(singletons["maximum"] == bound["sigma_upper"] == sigma,
                            "sharp unrestricted signed sensitivity")
                    d["singletons"] = singletons
                    d["sigma_exact"] = sigma
                if cap == selected_cap:
                    d["scalar_mutations"] = fanout.scalar_mutation_checks(
                        cc, circuit, layout, proof, loads)
                    rng = random.Random(4521)
                    mutations = []
                    for count in (1, 2, 7, 31, 128, 1024):
                        changed = proof.copy()
                        errors = rng.sample(range(layout.num_tags*128), count)
                        for address in errors:
                            tag, seed = divmod(address, 128)
                            changed[tag] ^= 1 << seed
                        failures = layout.failures(changed)
                        require(failures <= sigma * count, "mixed error bound")
                        mutations.append({"wrong_bits": count, "failed_pairs": failures})
                    d["mixed_errors"] = mutations
            summary["no" if no else "yes"] = d
        result["layouts"][str(cap)] = summary
    result["scope"] = "Finite compiler checks and inherited gate-charge upper bound; NO optimum not asserted."
    return result


def main():
    result = {"radius_1": check_radius(1, (2, 21)),
              "radius_2": check_radius(2, (2, 27, 62)),
              "cross": check_radius("cross", (2, 21))}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
