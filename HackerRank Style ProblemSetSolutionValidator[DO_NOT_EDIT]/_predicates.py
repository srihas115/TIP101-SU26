# ==============================================================================
#  PROBLEM SET SOLUTION VALIDATOR PREDICATES  —  DO NOT EDIT  ·  DO NOT DELETE
# ==============================================================================
#  Some problems accept ANY valid answer (e.g. "return any ordering with the
#  evens before the odds"). For those, we can't compare to a single stored
#  answer — instead we check the output against a predicate that defines what
#  "valid" means. These predicates verify structure only; they contain no
#  hidden answer keys.
#
#  Each predicate: pred(original_args: list, output) -> bool
#  (original_args is a fresh copy of the inputs, taken before the call, so it is
#  safe to use even when the graded function mutates its input.)
# ==============================================================================


def parity_partition(args, output):
    """Output is a rearrangement of nums with every even value before every odd."""
    nums = args[0]
    if not isinstance(output, list):
        return False
    if sorted(output) != sorted(nums):
        return False
    seen_odd = False
    for x in output:
        if x % 2 != 0:
            seen_odd = True
        elif seen_odd:
            return False
    return True


def parity_by_index(args, output):
    """Output is a rearrangement of nums where value parity matches index parity
    (even value at even index, odd value at odd index)."""
    nums = args[0]
    if not isinstance(output, list) or sorted(output) != sorted(nums):
        return False
    for i, v in enumerate(output):
        if v % 2 != i % 2:
            return False
    return True


# ------------------------------------------------------------------------------
#  Linked-list predicates.  These receive the BUILT node structures (the same way
#  the engine calls them), so they read values by walking pointers. All traversal
#  is cycle-safe (bounded by a seen-set) so a malformed result can't hang.
# ------------------------------------------------------------------------------

def _val(node):
    for attr in ("value", "val", "data"):
        if hasattr(node, attr):
            return getattr(node, attr)
    return None


def _walk_values(head, limit=100000):
    """Follow .next collecting values, stopping when a node repeats (handles both
    plain and circular lists). Returns (values, is_circular)."""
    vals = []
    seen = set()
    node = head
    while node is not None and count_ok(len(vals), limit):
        if id(node) in seen:
            return vals, (node is head)
        seen.add(id(node))
        vals.append(_val(node))
        node = getattr(node, "next", None)
    return vals, False


def count_ok(n, limit):
    return n < limit


def partition_around(args, output):
    """`partition(head, val)`: output is any ordering where every value < val
    comes before every value >= val, preserving the multiset of values."""
    val = args[1]
    src, _ = _walk_values(args[0])
    out, circ = _walk_values(output)
    if circ or sorted(out) != sorted(src):
        return False
    seen_ge = False
    for x in out:
        if x >= val:
            seen_ge = True
        elif seen_ge:          # a value < val appeared after a value >= val
            return False
    return True


def circular_after(args, output):
    """`make_circular(head)`: output must be a circular list (tail links to head)
    holding exactly the original values in the original order."""
    src, _ = _walk_values(args[0])
    out, circ = _walk_values(output)
    if not src:                       # empty list: nothing to make circular
        return output is None or out == []
    return circ and out == src


def circular_delete(args, output):
    """`delete_node(head, val)` on a circular list: output is still circular and
    equals the original values with the first occurrence of val removed."""
    val = args[1]
    src, _ = _walk_values(args[0])
    expected = list(src)
    if val in expected:
        expected.remove(val)
    out, circ = _walk_values(output)
    if not expected:                  # list became empty
        return output is None or out == []
    return circ and out == expected


# ------------------------------------------------------------------------------
#  Review-unit predicates (Unit 10): problems that accept any valid answer.
# ------------------------------------------------------------------------------

def anagram_groups(args, output):
    """Output groups the input strings so that two strings share a group iff they
    are anagrams (order of groups and within groups doesn't matter)."""
    strs = args[0]
    if not isinstance(output, list):
        return False
    flat = []
    for g in output:
        if not isinstance(g, list):
            return False
        flat.extend(g)
    if sorted(flat) != sorted(strs):
        return False

    def key(s):
        return tuple(sorted(s))
    for g in output:                       # each group is internally consistent
        if len({key(s) for s in g}) > 1:
            return False
    group_keys = [key(g[0]) for g in output if g]
    return len(group_keys) == len(set(group_keys))   # anagrams fully merged


def custom_sorted(args, output):
    """Output is a permutation of s in which the characters that appear in `order`
    keep order's relative ordering (others may go anywhere)."""
    order, s = args[0], args[1]
    if not isinstance(output, str) or sorted(output) != sorted(s):
        return False
    idxs = [order.index(c) for c in output if c in order]
    return idxs == sorted(idxs)


def sum_pair(args, output):
    """Output is [a, b, c, d] drawn from numbers with a + b == c + d, or [] only if
    no such four elements (at 4 distinct positions) exist."""
    from collections import Counter
    nums = args[0]
    if output == []:
        by_sum = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                for (pi, pj) in by_sum.get(s, []):
                    if len({pi, pj, i, j}) == 4:
                        return False       # a valid answer existed
                by_sum.setdefault(s, []).append((i, j))
        return True
    if not isinstance(output, list) or len(output) != 4:
        return False
    a, b, c, d = output
    if a + b != c + d:
        return False
    have, need = Counter(nums), Counter(output)
    return all(have[k] >= v for k, v in need.items())


def _node_val(node):
    for attr in ("val", "value", "data"):
        if hasattr(node, attr):
            return getattr(node, attr)
    return None


def leaf_layers(args, output):
    """Output is the successive layers of leaves peeled off the tree (order within a
    layer doesn't matter). Recomputed from the original tree and compared."""
    root = args[0]
    layers = {}

    def height(n):
        if n is None:
            return -1
        h = 1 + max(height(getattr(n, "left", None)), height(getattr(n, "right", None)))
        layers.setdefault(h, []).append(_node_val(n))
        return h
    height(root)
    expected = [sorted(layers[k]) for k in sorted(layers)]
    if not isinstance(output, list) or len(output) != len(expected):
        return False
    got = [sorted(g) for g in output]
    return got == expected


def _walk_ring(node, limit=100000):
    vals, seen = [], set()
    cur = node
    while cur is not None and len(vals) < limit:
        if id(cur) in seen:
            return vals, True
        seen.add(id(cur))
        vals.append(_node_val(cur))
        cur = getattr(cur, "next", None)
    return vals, False


def sorted_circular_insert(args, output):
    """After insert(start_node, insert_val) the ring is still circular, still sorted
    (some rotation is non-decreasing), and holds the original values plus the new one."""
    start, insert_val = args[0], args[1]
    original, _ = _walk_ring(start) if start is not None else ([], True)
    out, is_ring = _walk_ring(output)
    if not is_ring and len(out) > 1:
        return False
    if sorted(out) != sorted(original + [insert_val]):
        return False
    # some rotation must be non-decreasing (a sorted circular list)
    n = len(out)
    for r in range(n):
        rot = out[r:] + out[:r]
        if all(rot[i] <= rot[i + 1] for i in range(n - 1)):
            return True
    return n <= 1


PREDICATES = {
    "parity_partition": parity_partition,
    "parity_by_index": parity_by_index,
    "partition_around": partition_around,
    "circular_after": circular_after,
    "circular_delete": circular_delete,
    "anagram_groups": anagram_groups,
    "custom_sorted": custom_sorted,
    "sum_pair": sum_pair,
    "leaf_layers": leaf_layers,
    "sorted_circular_insert": sorted_circular_insert,
}
