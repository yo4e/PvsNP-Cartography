"""Shape formula versus full physical leaf addresses (standard-library Python 3)."""
from pathlib import Path
import importlib.util
import json
import sys


def require(condition, message):
    if not condition:
        raise ValueError(message)


def blocks(k, a):
    leaves, siblings = [], []

    def visit(tokens):
        if len(tokens) <= 2*a:
            block = tuple(i for i in tokens if i is not None)
            leaves.append(block)
            return block
        low = len(tokens)//2
        left = visit(tokens[:low]+[None]*a)
        right = visit(tokens[low:])
        siblings.append((left, right))
        return left
    visit(list(range(k)))
    require(sorted(i for leaf in leaves for i in leaf) == list(range(k)), "token partition")
    return leaves, siblings


def support(points):
    result = [0]
    for i in points:
        result += [x | (1 << i) for x in result]
    return result


def base_masks(k, a):
    leaves, pairs = blocks(k, a)
    one = [(1 << len(x))-1 for x in leaves]
    two = [((1 << len(x))-1)*((1 << len(y))-1) for x, y in pairs]
    result = set().union(*(support(b) for b in leaves), *(support(x+y) for x, y in pairs))
    require(len(result) == 1+sum(one)+sum(two), "overlap count")
    return result


def leaf_words(d, a, point, stack=()):
    """Enumerate complete leaves. A frame holds side, parent dimension, edge label."""
    if d <= 2*a:
        yield stack, d
        return
    lo = d//2
    low = point % (1 << lo)
    high = point >> lo
    row = stack + (("row", d, high),)
    for pad in range(1 << a):
        yield from leaf_words(lo+a, a, low | (pad << lo), row)
    for pad in range(1 << (a-1)):
        label = low | (pad << lo)
        yield from leaf_words(d-lo, a, high, stack+(("column", d, label),))


def physical(stack, point, a):
    """Reference ascent at an absolute leaf position, following actual aliases."""
    for i in reversed(range(len(stack))):
        side, d, label = stack[i]
        lo = d//2
        if side == "column":
            return stack[:i]+(("row", d, point),), label | (1 << (lo+a-1))
        if point >> lo:
            return stack[:i+1], point
        point |= label << lo
    return (), point


def full_view(k, a, seed):
    result = set()
    for stack, d in set(leaf_words(k, a, seed)):
        result.update(physical(stack, point, a) for point in range(1 << d))
    require(((), seed) in result, "own physical root")
    return result


def algebraic_fixture():
    source = Path(__file__).resolve().parent.parent/"041-two-level-distance"/"two_level_oracle.py"
    spec = importlib.util.spec_from_file_location("actual_two_level_geometry", source)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    leaves = mod.geometry()
    sets = [set().union(*(leaves[x].addresses for x in mod.selected(z))) for z in range(256)]
    for H in [(0,), (0, 1, 2), (0, 9), (0, 9, 18, 27)]:
        K = {x^h^j for x in base_masks(8, 3) for h in H for j in H}
        combined = [set().union(*(sets[z^h] for h in H)) for z in range(256)]
        # Inverted incidence gives every intersection without quadratic cell scans.
        touching = {}
        for z, view in enumerate(combined):
            for addr in view:
                touching.setdefault(addr, set()).add(z)
        for z, view in enumerate(combined):
            observed = set().union(*(touching[addr] for addr in view))
            require(observed=={z^x for x in K}, "field fixture overlap")
    return {"physical_cells":mod.WORD_COUNT, "centers_per_mask_set":256, "mask_sets":4}


def replay(k, a, differences):
    K = base_masks(k, a)
    zero = full_view(k,a,0)
    centers = [0, (1 << k)-1]
    count = 0
    for c in centers:
        other = zero if c == 0 else full_view(k,a,c)
        for z in differences:
            actual = not other.isdisjoint(full_view(k,a,z^c))
            require(actual == (z in K), f"physical collision k={k} c={c} displacement={z}")
            count += 1
    return {"k":k,"a":a,"base_overlap":len(K),"differences_per_center":len(differences),"checks":count}


def main():
    replays = [replay(k, 3, range(1<<k)) for k in (7,8,9)]
    # Root column recurses, and this branch has both passing and failing offsets.
    k=13
    K=base_masks(k, 3)
    ordered=sorted(K)
    outside=sorted(set(range(1<<k))-K)
    sample=set(ordered[::max(1,len(ordered)//32)]+outside[::max(1,len(outside)//32)])
    leaves, pairs=blocks(k,3)
    sample.update(sum(1<<i for i in x+y) for x,y in pairs)
    replays.append(replay(k,3,sorted(sample)))
    counts=[]
    for k in (8,10,11,12,13,14,32,64,128):
        K=base_masks(k,3)
        H=(0,9,18,27)
        J={x^h for x in K for h in H}
        counts.append({"k":k,"single":len(K),"four":len(J)})
    n=1<<64
    d=n//8
    s=next(x["four"] for x in counts if x["k"]==64)
    print(json.dumps({"physical_coordinates":replays, "GF256_fixture":algebraic_fixture(),
                      "formula_counts":counts, "m_at_k64":min(d,n-3*s-1,(n-d-4)//s)},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
