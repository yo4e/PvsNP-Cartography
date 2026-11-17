"""Decode two nonconstant polynomials from the physically shared GF(256) fixture."""
import argparse
import importlib.util
import json
import sys
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_oracle(path):
    spec = importlib.util.spec_from_file_location("two_level_reference", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def newton(field, nodes, values):
    coefficients = list(values)
    for gap in range(1, len(nodes)):
        for i in range(len(nodes)-1, gap-1, -1):
            difference = coefficients[i] ^ coefficients[i-1]
            coefficients[i] = field.mul(difference, field.inv(nodes[i] ^ nodes[i-gap]))
    return coefficients


def evaluate(field, nodes, coefficients, x):
    result = 0
    for node, c in reversed(list(zip(nodes, coefficients))):
        result = c ^ field.mul(x ^ node, result)
    return result


def replay(oracle):
    leaves = oracle.geometry()
    # Adding a single consistent nonconstant extension to the old split witness
    # preserves every leaf verdict by linearity. Still check the actual leaves.
    cells = [a ^ b for a, b in zip(oracle.templates(), oracle.legal_extension(31))]
    verdict = {key: oracle.leaf_passes(cells, leaf) for key, leaf in leaves.items()}
    accepted = {x for x in range(256) if all(verdict[k] for k in oracle.selected(x))}
    polynomial_tables = []
    for p in (0, 1):
        good_rows = [v for v in range(16)
                     if all(verdict["inner_row", v, p+2*f] for f in range(8))
                     and sum(all(verdict["inner_col", v, b+8*h] for h in range(4))
                             for b in range(8)) >= 2]
        require(len(good_rows) == 8, "passing rows")
        columns = [c for c in range(64) if (c//8) % 2 == p and verdict["outer_col", c]]
        require(len(columns) == 32, "passing columns")
        column_nodes = [oracle.OUTER_AUX[0] ^ oracle.vector((*oracle.ROOT_BASIS[:4],
                        *oracle.OUTER_AUX[1:]), c) for c in columns[:16]]
        sample_rows = good_rows[:2]
        y_nodes = [leaves["outer_col", 0].points[v] for v in sample_rows]
        columns_in_y = [newton(oracle, y_nodes,
                        [cells[leaves["outer_col", c].addresses[v]] for v in sample_rows])
                        for c in columns[:16]]
        table = []
        for v, ordinate in enumerate(leaves["outer_col", 0].points):
            row_values = [evaluate(oracle, y_nodes, coeff, ordinate) for coeff in columns_in_y]
            row_in_x = newton(oracle, column_nodes, row_values)
            for u in range(16):
                x = 16*v+u
                value = evaluate(oracle, column_nodes, row_in_x, oracle.THETA ^ x)
                require(value == oracle.field_power(x, 31) ^ p,
                        "reconstructed extension disagrees with planted root polynomial")
                table.append(value)
        polynomial_tables.append(table)

    covered = [set(x for x in accepted if table[x] == cells[x]) for table in polynomial_tables]
    require(covered[0] | covered[1] == accepted and len(accepted) == 128, "site cover")
    require(len(covered[0]) == len(covered[1]) == 64 and not (covered[0] & covered[1]),
            "expected disjoint scope of this witness")
    # Subtracting the planted X^31, a single degree-<32 cover would need
    # to vanish at 64 sites and equal 1 on the other 64.
    return {"degree_of_each_reconstructed_polynomial": 31,
            "agreement_on_accepted_sites": list(map(len, covered)),
            "size_of_union_on_accepted_sites": len(covered[0] | covered[1]),
            "base_field_polynomial_table_entries_checked": 512}


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument("--oracle", type=Path,
                        default=here.parent/"041-two-level-distance"/"two_level_oracle.py")
    args = parser.parse_args()
    print(json.dumps(replay(load_oracle(args.oracle)), indent=2, sort_keys=True))
