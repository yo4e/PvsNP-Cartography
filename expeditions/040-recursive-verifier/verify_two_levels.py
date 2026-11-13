"""Exact seed schedule for (k,a)=(8,3) and a single faulty auxiliary symbol."""
import json

def require(condition, message):
    if not condition:
        raise ValueError(message)


def leaves(z):
    """Return second-level (row, column) labels inside the selected outer row."""
    low = z & 15
    checked_rows = set()
    checked_columns = set()
    for outer_fresh in range(8):
        child_seed = low | (outer_fresh << 4)
        checked_rows.add(child_seed >> 3)
        for inner_fresh in range(4):
            checked_columns.add((inner_fresh << 3) | (child_seed & 7))
    return checked_rows, checked_columns


def main():
    bad_outer_row = 4
    bad_inner_row = 3
    bad_slot = 8  # Extension in this row, outside the parent and common columns.
    require(8 <= bad_slot < 32, "wrong rectangle")
    rejected = []
    for z in range(256):
        rows, columns = leaves(z)
        require(len(rows) == 8 and all((b & 1) == ((z >> 3) & 1) for b in rows),
                "inner row group lost its dependence on bit 3")
        require(columns == {8 * b + (z & 7) for b in range(4)}, "wrong column group")
        if z >> 4 == bad_outer_row and bad_inner_row in rows:
            rejected.append(z)
    require(rejected == list(range(72, 80)), "unexpected public rejection set")
    return {"root_dimension": 8, "row_child_dimension": 7,
            "fault": {"outer_row": bad_outer_row, "inner_row": bad_inner_row, "slot": bad_slot},
            "checks_per_selected_outer_row": {"inner_rows": 8, "inner_columns": 4},
            "rejecting_public_seeds": rejected,
            "root_relative_distance": "0", "rs_rejection_probability": "1/32"}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
