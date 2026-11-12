"""Exhaustively compare glued scores with every global Boolean proof.

F is a sum, not an average across clauses. Integer scores below count in
units of one over the number of seeds. The images and their masses come
from enumerating the actual projection maps. This is a finite control.
"""

import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, product


def require(condition, message):
    if not condition:
        raise ValueError(message)


# A read is (positive, low address coordinate, high address coordinate).
# x and y denote independent bits in the uniform two-bit seed.
FAMILIES = {
    "opposite_units_permuted_seeds": [
        [(True, "x", "y")],
        [(False, "!x", "y")],
    ],
    "opposite_units_unequal_ranks": [
        [(True, "x", "y")],
        [(False, "!y", "0")],
    ],
    "crossing_nested_and_diagonal_images": [
        [(True, "x", "0"), (False, "0", "y")],
        [(True, "x", "x"), (False, "y", "!x")],
    ],
    "constant_repeated_and_opposite_literals": [
        [(True, "0", "0")],
        [(False, "x", "!x")],
        [(False, "!x", "1"), (True, "!x", "1"), (True, "x", "0")],
    ],
}


def addresses(read):
    _, low, high = read
    result = []
    for seed in range(4):
        x = seed & 1
        y = seed >> 1
        bits = {"0": 0, "1": 1, "x": x, "y": y, "!x": 1 - x, "!y": 1 - y}
        result.append(bits[low] + 2 * bits[high])
    return result


def global_score(clauses, proof):
    failures = 0
    for clause in clauses:
        reads = [(positive, addresses((positive, low, high))) for positive, low, high in clause]
        for seed in range(4):
            if all(bool((proof >> query[seed]) & 1) != positive for positive, query in reads):
                failures += 1
    return failures


def exhaust_family(clauses):
    occurrences = [read for clause in clauses for read in clause]
    queries = [addresses(read) for read in occurrences]
    weights = [Counter(values) for values in queries]
    images = [sorted(mass) for mass in weights]
    for mass in weights:
        require(len(set(mass.values())) == 1, "projection has nonuniform image")

    local_options = []
    for addresses_in_image in images:
        options = []
        for values in product((0, 1), repeat=len(addresses_in_image)):
            options.append(dict(zip(addresses_in_image, values)))
        local_options.append(options)

    scores = {proof: global_score(clauses, proof) for proof in range(16)}
    best = min(scores.values())
    honest_proofs = [proof for proof, score in scores.items() if score == 0]
    overlaps = [(j, l, address, min(weights[j][address], weights[l][address]))
                for j, l in combinations(range(len(occurrences)), 2)
                for address in weights[j].keys() & weights[l].keys()]
    local_count = strict_repair = tight_repair = yes_tests = 0
    for tables in product(*local_options):
        local_count += 1
        first = 0
        local_failures = 0
        for clause in clauses:
            for seed in range(4):
                literals = [bool(tables[j][queries[j][seed]]) == occurrences[j][0]
                            for j in range(first, first + len(clause))]
                local_failures += int(not any(literals))
            first += len(clause)

        disagreement = sum(mass for j, l, a, mass in overlaps if tables[j][a] != tables[l][a])
        score = local_failures + disagreement
        require(best <= score, "a local glued score beats every global proof")
        if local_failures < best:
            strict_repair += 1
            tight_repair += int(score == best)
        for proof in honest_proofs:
            errors = sum(mass for j, weights_j in enumerate(weights)
                         for a, mass in weights_j.items() if tables[j][a] != ((proof >> a) & 1))
            require(score <= len(tables) * errors, "YES score exceeds occurrence error budget")
            yes_tests += 1

    return {
        "clauses": len(clauses), "occurrences": len(occurrences),
        "image_sizes": [len(points) for points in images],
        "min_global_F": str(Fraction(best, 4)),
        "local_families_tested": local_count, "honest_proofs": len(honest_proofs),
        "yes_comparisons": yes_tests,
        "families_below_global_before_repair": strict_repair,
        "of_those_tight_after_adding_D": tight_repair,
    }


def independent_collision(k):
    # Two opposite units on the same identity image, H_+=1 and H_-=0.
    # Every global proof incurs one failed unit per seed.
    size = 1 << k
    collisions = sum(a == b for a in range(size) for b in range(size))
    product_score = Fraction(collisions, size * size)
    shared_score = sum(Fraction(1, size) for _ in range(size))
    require(product_score == Fraction(1, size), "wrong independent collision frequency")
    require(shared_score == 1 and product_score < shared_score, "collision attack failed")
    return {"seed_bits": k, "local_F": 0, "minimum_global_F": 1,
            "shared_address_D": str(shared_score), "independent_seed_penalty": str(product_score)}


if __name__ == "__main__":
    print(json.dumps({"families": {name: exhaust_family(clauses) for name, clauses in FAMILIES.items()},
                      "collision_controls": [independent_collision(k) for k in (1, 2, 4, 8)]},
                     indent=2))
