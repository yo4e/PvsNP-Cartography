"""Cost and signed-error controls for the actual Expedition 040 compiler."""
from array import array
from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import product
from pathlib import Path
import argparse
import copy
import hashlib
import json
import random
import sys


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_reference(source):
    sys.path.insert(0, str(source))
    import clause_compiler
    import recursive_rs
    import verify_verifier
    return clause_compiler, recursive_rs, verify_verifier


class CopyCircuit:
    """Private copy trees preserve all original physical input keys and signs."""

    def __init__(self, source, cap, reference):
        require(cap >= 2, "fanout cap")
        self.source = source
        self.reference = reference
        self.cap = cap
        self.one, self.zero = source.one, source.zero
        self.inputs = source.inputs.copy()
        self.public = list(source.public)
        self.size = source.size
        self.gates = []
        self.physical = {wire for key, wire in self.inputs.items() if key[0] in ("A", "B")}
        self.demands = Counter(abs(lit) for _, a, b, _ in source.gates for lit in (a, b))
        self.demands[abs(source.output)] += 1
        self.routes = {}
        self.next_use = Counter()
        self.copy_count = 0
        for wire in source.inputs.values():
            self.prepare(wire)
        for op, a, b, c in source.gates:
            self.gates.append((op, self.consume(a), self.consume(b), c))
            self.prepare(c)
        self.output = self.consume(source.output)
        require(self.next_use == self.demands, "every original occurrence routed once")
        fanout = Counter()
        for op, a, b, _ in self.gates:
            fanout[abs(a)] += 1
            if op != "copy":
                fanout[abs(b)] += 1
        fanout[abs(self.output)] += 1
        require(all(fanout[w] == int(self.demands[w] > 0) for w in self.physical),
                "one read root per used physical map")
        require(all(value <= cap for w, value in fanout.items() if w not in self.physical),
                "private fanout cap")
        self.fanout = fanout

    def copy(self, wire):
        self.size += 1
        self.gates.append(("copy", wire, 0, self.size))
        self.copy_count += 1
        return self.size

    def prepare(self, wire):
        count = self.demands[wire]
        if not count:
            self.routes[wire] = []
            return
        current = self.copy(wire) if wire in self.physical else wire
        route = []
        while count > self.cap:
            route.extend([current] * (self.cap - 1))
            count -= self.cap - 1
            current = self.copy(current)
        route.extend([current] * count)
        self.routes[wire] = route

    def consume(self, literal):
        wire = abs(literal)
        position = self.next_use[wire]
        self.next_use[wire] += 1
        replacement = self.routes[wire][position]
        return replacement if literal > 0 else -replacement

    def templates(self):
        yield (self.one,)
        for op, a, b, c in self.gates:
            if op == "copy":
                yield (-a, c)
                yield (a, -c)
            else:
                yield from self.reference.gate_clauses(op, a, b, c)
        yield (self.output,)

    def evaluate(self, a, cells):
        original = self.source.evaluate(a, cells)
        values = [0] * (self.size + 1)
        known = set(self.inputs.values())
        for wire in known:
            values[wire] = original[wire]
        for op, left, right, output in self.gates:
            require(abs(left) in known and (op == "copy" or abs(right) in known),
                    "topological evaluation")
            u = self.reference.signed(values, left)
            if op == "copy":
                values[output] = u
            else:
                v = self.reference.signed(values, right)
                values[output] = u ^ v if op == "xor" else u & v
            known.add(output)
        require(self.reference.signed(values, self.output) ==
                self.reference.signed(original, self.source.output), "same public-seed verdicts")
        return values


def census(circuit, layout):
    operations = Counter(op for op, *_ in circuit.gates)
    rows = 1 << (layout.num_tags - 1).bit_length()
    return {"gates": dict(sorted(operations.items())), "used_physical_rows": layout.num_tags,
            "padded_physical_rows": rows, "Q": 128 * rows,
            "clause_templates": layout.template_count,
            "clause_seed_pairs": 128 * layout.template_count}


def singleton_loads(reference, circuit, layout, values):
    """Exact F({cell}) at a satisfying reference, keeping clause multiplicities."""
    require(layout.failures(layout.pack_assignment(values)) == 0, "satisfying reference")
    loads = array("I", [0]) * (layout.num_tags * 128)
    for clause in layout.templates:
        require(len({layout.read[abs(lit)] for lit in clause}) == len(clause),
                "different physical literals inside one template")
        truth = [reference.signed(values, lit) for lit in clause]
        for i, literal in enumerate(clause):
            sole = truth[i]
            for j, word in enumerate(truth):
                if j != i:
                    sole &= reference.FULL ^ word
            tag, offset = layout.read[abs(literal)]
            while sole:
                least = sole & -sole
                seed = least.bit_length() - 1
                loads[(tag << 7) + (seed ^ offset)] += 1
                sole ^= least
    for wire in circuit.public:
        tag, _ = layout.read[wire]
        for seed in range(128):
            loads[(tag << 7) + seed] += 2
    maximum = max(loads)
    address = loads.index(maximum)
    witness_tag, witness_seed = divmod(address, 128)
    proof = layout.pack_assignment(values)
    proof[witness_tag] ^= 1 << witness_seed
    require(layout.failures(proof) == maximum, "actual maximum singleton replay")
    roles = {wire: key[0] for key, wire in circuit.inputs.items()}
    by_role = {}
    for wire, (tag, _) in layout.read.items():
        role = roles.get(wire, "gate")
        by_role[role] = max(by_role.get(role, 0), max(loads[tag*128:(tag+1)*128]))
    return {"maximum": maximum, "witness_tag": witness_tag, "witness_seed": witness_seed,
            "direct_failed_pairs": maximum, "maxima_by_role": by_role}, loads


def uniform_signed_bound(circuit, layout):
    physical = Counter()
    private = Counter()
    for wire in circuit.physical:
        if circuit.demands[wire]:
            physical[layout.read[wire][0]] += 1
    for op, _, _, output in circuit.gates:
        private[output] += 2 if op == "and" else 1
    private[circuit.one] += 1
    for wire in circuit.public:
        private[wire] += 2
    for wire, count in circuit.fanout.items():
        if wire not in circuit.physical:
            private[wire] += count
    return {"physical_input_bound": max(physical.values()),
            "private_and_pin_bound": max(private.values()),
            "sigma_upper": max(max(physical.values()), max(private.values()))}


def gate_error_checks(reference):
    checks = 0
    for op in ("and", "xor", "copy"):
        for first, second in ((1, 2), (1, 1), (1, -1)):
            for sign_a, sign_b in product((-1, 1), repeat=2):
                a, b = sign_a*first, sign_b*second
                for x, y in product((0, 1), repeat=2):
                    before = [None, x, y, None]
                    av = before[abs(a)] ^ int(a < 0)
                    bv = before[abs(b)] ^ int(b < 0)
                    before[3] = av & bv if op == "and" else av ^ bv if op == "xor" else av
                    clauses = ((-a, 3), (a, -3)) if op == "copy" else reference.gate_clauses(op, a, b, 3)
                    for error in range(8):
                        after = [None, *(before[w] ^ ((error >> (w-1)) & 1) for w in (1, 2, 3))]
                        missed = sum(not any(after[abs(lit)] == (lit > 0) for lit in clause)
                                     for clause in clauses)
                        ea = (error >> (abs(a)-1)) & 1
                        eb = (error >> (abs(b)-1)) & 1
                        ec = (error >> 2) & 1
                        cost = ea + (0 if op == "copy" else eb) + (2 if op == "and" else 1)*ec
                        require(missed <= cost, "local signed error charge including aliases")
                        actual_a = after[abs(a)] ^ int(a < 0)
                        actual_b = after[abs(b)] ^ int(b < 0)
                        expected = (actual_a & actual_b if op == "and" else actual_a ^ actual_b
                                    if op == "xor" else actual_a)
                        require((missed == 0) == (after[3] == expected), "equivalence gate semantics")
                        checks += 1
    changed = [None, 0, 0, 1]
    witness = sum(not any(changed[abs(lit)] == (lit > 0) for lit in clause)
                  for clause in reference.gate_clauses("and", 1, 2, 3))
    require(witness == 2, "AND output needs charge two")
    return {"signed_and_alias_cases": checks, "AND_000_to_001_failed_clauses": witness}


def greedy_true_certificate(reference, layout, values, initial):
    """Regeneratable completion of the mandatory singleton true-literal assignment."""
    loads = array("I", initial)
    proof = layout.pack_assignment(values)
    digest = hashlib.sha256()
    completion_count = 0
    for clause in layout.templates:
        truths = [reference.signed(values, lit) for lit in clause]
        multiple = 0
        for i, truth in enumerate(truths):
            for j in range(i):
                multiple |= truth & truths[j]
        while multiple:
            low = multiple & -multiple
            seed = low.bit_length() - 1
            candidates = []
            for literal, truth in zip(clause, truths):
                if truth & low:
                    tag, offset = layout.read[abs(literal)]
                    address = (tag << 7) + (seed ^ offset)
                    candidates.append((address, literal))
            address, literal = min(candidates, key=lambda pair: loads[pair[0]])
            tag, point = divmod(address, 128)
            require(((proof[tag] >> point) & 1) == (literal > 0), "charged physical literal is true")
            loads[address] += 1
            digest.update(address.to_bytes(4, "little"))
            completion_count += 1
            multiple ^= low
    mass = sum(loads)
    require(mass == layout.template_count * 128, "all clause-seed pairs charged once including pins")
    return {"maximum_true_literal_load": max(loads), "total_assigned_clause_seed_pairs": mass,
            "greedy_completion_choices": completion_count,
            "completion_address_stream_sha256": digest.hexdigest()}


def scalar_mutation_checks(reference, circuit, layout, proof, loads):
    """Scalar physical-address evaluation of every pair touched by each mutation."""
    addresses = [loads.index(max(loads))]
    pin_tag = layout.read[circuit.public[0]][0]
    addresses.append(pin_tag * 128 + 17)
    gate = next(c for op, _, _, c in circuit.gates if op == "and")
    addresses.append(layout.read[gate][0]*128 + 9)
    observed = []
    for changed in addresses:
        changed_tag, point = divmod(changed, 128)
        candidates = []
        for clause in layout.templates:
            seeds = {point ^ layout.read[abs(lit)][1] for lit in clause
                     if layout.read[abs(lit)][0] == changed_tag}
            candidates.extend(tuple(layout.address(lit, seed) for lit in clause) for seed in sorted(seeds))
        for seed in range(128):
            for i, wire in enumerate(circuit.public):
                for bit in (0, 1):
                    clamped = (seed & ~(1 << i)) | (bit << i)
                    literal = layout.address(wire if bit else -wire, clamped)
                    if abs(literal)-1 == changed:
                        candidates.append((literal,))
        count = 0
        for clause in candidates:
            satisfied = False
            for literal in clause:
                address = abs(literal)-1
                tag, seed = divmod(address, 128)
                bit = (proof[tag] >> seed) & 1
                bit ^= address == changed
                satisfied |= bit == (literal > 0)
            count += not satisfied
        require(count == loads[changed], "scalar physical mutation count")
        observed.append({"address": changed, "failed_pairs": count,
                         "touched_clause_seed_pairs": len(candidates)})
    return observed


def bypass_copy(circuit, driver):
    """Mutant removes one consistency copy and reconnects its outgoing literals."""
    target = next(c for op, a, _, c in circuit.gates if op == "copy" and a == driver)
    mutant = copy.copy(circuit)
    def replace(literal):
        return (driver if literal > 0 else -driver) if abs(literal) == target else literal
    mutant.gates = [(op, replace(a), replace(b), c) for op, a, b, c in circuit.gates if c != target]
    mutant.output = replace(circuit.output)
    return mutant


def omitted_copy_controls(reference, circuit, a, cells, old_layout, old_loads):
    physical = next(w for key, w in circuit.inputs.items() if key == ("A", 0, 0, 0))
    gate_outputs = {c for _, _, _, c in circuit.source.gates}
    driver = max(gate_outputs, key=lambda w: circuit.demands[w])
    output = {}
    for name, wire in (("physical_boundary", physical), ("private_fanout_split", driver)):
        mutant = bypass_copy(circuit, wire)
        layout = reference.PhysicalCNF(mutant)
        values = mutant.evaluate(a, cells)
        proof = layout.pack_assignment(values)
        require(layout.failures(proof) == 0, "mutant preserves honest function")
        old_tag = old_layout.read[wire][0]
        scores = old_loads[old_tag*128:(old_tag+1)*128]
        seed = scores.index(max(scores))
        tag = layout.read[wire][0]
        proof[tag] ^= 1 << seed
        failed = layout.failures(proof)
        require(failed > 128, "omitted consistency feature violates proposed bound")
        output[name] = {"flipped_wire": wire, "seed": seed, "failed_pairs": failed}
    return output


def small_semantics(reference):
    """Exhaust all private assignments on one signed two-gate test with sharing."""
    class Tiny:
        def __init__(self):
            self.one, self.zero, self.size = 1, -1, 4
            self.inputs = {("constant",): 1, ("A", 0, 0, 0): 2}
            self.public = []
            self.gates = [("xor", 2, 1, 3), ("and", 2, -3, 4)]
            self.output = 4
    transformed = CopyCircuit(Tiny(), 2, reference)
    clauses = tuple(transformed.templates())
    require(transformed.copy_count == 1, "small fanout copy")
    results = []
    for physical in (0, 1):
        minimum = len(clauses)
        for table in product((0, 1), repeat=transformed.size-1):
            values = [None, *table[:1], physical, *table[1:]]
            require(len(values) == transformed.size+1, "small assignment width")
            failed = sum(not any(values[abs(lit)] == (lit > 0) for lit in clause) for clause in clauses)
            minimum = min(minimum, failed)
        require(minimum == 1-physical, "private copy tree output soundness")
        results.append(minimum)
    return {"private_assignments_each": 1 << (transformed.size-1), "minima_input_0_1": results}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1] /
                        "040-recursive-verifier")
    parser.add_argument("--scalar", action="store_true", help="include direct DIMACS-address controls")
    args = parser.parse_args()
    reference, rs, verifier = load_reference(args.source)
    result = {"local_gate_cases": gate_error_checks(reference), "small_private_semantics": small_semantics(reference)}
    fixtures = verifier.cases()
    yes_a, yes_cells = fixtures["perfect_yes"]
    original_yes = reference.BitCircuit().compile(False)
    old_layout = reference.PhysicalCNF(original_yes)
    old_values = original_yes.evaluate(yes_a, yes_cells)
    old_singleton, old_loads = singleton_loads(reference, original_yes, old_layout, old_values)
    certificate = greedy_true_certificate(reference, old_layout, old_values, old_loads)
    require(certificate["maximum_true_literal_load"] == old_singleton["maximum"] == 288,
            "exact old signed sensitivity certificate")
    result["original_yes"] = census(original_yes, old_layout) | {"singletons": old_singleton,
            "true_literal_certificate": certificate, "sigma_exact_for_reference": 288}
    if args.scalar:
        result["original_yes"]["scalar_mutations"] = scalar_mutation_checks(reference, original_yes,
                old_layout, old_layout.pack_assignment(old_values), old_loads)
    result["copies"] = []
    for cap in (2, 126):
        summary = {"fanout_cap": cap, "cases": {}}
        for no in (False, True):
            source = reference.BitCircuit().compile(no)
            circuit = CopyCircuit(source, cap, reference)
            layout = reference.PhysicalCNF(circuit)
            original_layout = reference.PhysicalCNF(source)
            require(all(layout.read[w] == original_layout.read[w]
                        for w in circuit.physical), "original physical input aliases")
            comparisons = 0
            for a, cells in fixtures.values():
                circuit.evaluate(a, cells)
                comparisons += 1
            name = "no" if no else "yes"
            chosen_a, chosen_cells = fixtures["sharp_no" if no else "perfect_yes"]
            values = circuit.evaluate(chosen_a, chosen_cells)
            proof = layout.pack_assignment(values)
            expected_failures = 109 if no else 0
            require(layout.failures(proof) == expected_failures, "canonical NO/YES failed pairs")
            details = census(circuit, layout) | {"copy_rows": circuit.copy_count,
                        "field_assignments_compared": comparisons, "canonical_failed_pairs": expected_failures}
            if not no:
                singletons, loads = singleton_loads(reference, circuit, layout, values)
                bound = uniform_signed_bound(circuit, layout)
                require(singletons["maximum"] == bound["sigma_upper"] == 128, "exact signed sensitivity")
                details |= {"singletons": singletons, "signed_bound": bound}
                details["guaranteed_precision_gain"] = str(Fraction(
                    result["original_yes"]["Q"]*old_singleton["maximum"], details["Q"]*128))
                details["precision_threshold"] = str(Fraction(109, details["Q"]*128))
                if cap == 126:
                    details["omitted_copy_mutants"] = omitted_copy_controls(reference, circuit,
                            yes_a, yes_cells, old_layout, old_loads)
                if args.scalar and cap == 126:
                    details["scalar_mutations"] = scalar_mutation_checks(reference, circuit, layout, proof, loads)
                # Alter actual physical cells from several roles together, including padding-free tags.
                rng = random.Random(21128)
                details["mixed_error_set_sizes"] = [1, 2, 7, 31, 128]
                for error_count in details["mixed_error_set_sizes"]:
                    corrupted = proof.copy()
                    errors = rng.sample(range(layout.num_tags*128), error_count)
                    for address in errors:
                        tag, seed = divmod(address, 128)
                        corrupted[tag] ^= 1 << seed
                    require(layout.failures(corrupted) <= 128*error_count, "mixed actual physical error set")
            summary["cases"][name] = details
        result["copies"].append(summary)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
