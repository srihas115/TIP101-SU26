# ==============================================================================
#  PROBLEM SET SOLUTION VALIDATOR VISUALIZERS  —  DO NOT EDIT  ·  DO NOT DELETE
# ==============================================================================
#  Compact, dependency-free ASCII drawings of linked lists and binary trees so
#  students can *see* the structure their code produced, right in the terminal.
#  Pure standard library. Works on any machine, no installs.
#
#  Node shapes are detected structurally (duck typing) so this works no matter
#  what the student named their class — Node, ListNode, TreeNode, etc.
# ==============================================================================

from __future__ import annotations

_MAX_NODES = 40  # safety cap so a giant / cyclic structure never floods the terminal


def _get(node, *names):
    for n in names:
        if hasattr(node, n):
            return getattr(node, n)
    return None


def _has(node, *names):
    return any(hasattr(node, n) for n in names)


def is_tree_node(x) -> bool:
    return (hasattr(x, "left") and hasattr(x, "right")
            and _has(x, "val", "value", "data", "key"))


def is_list_node(x) -> bool:
    return (hasattr(x, "next") and not hasattr(x, "left")
            and _has(x, "val", "value", "data"))


def _node_val(node) -> str:
    return str(_get(node, "val", "value", "data", "key"))


# ------------------------------------------------------------------------------
#  Linked lists:   a → b → c → None
# ------------------------------------------------------------------------------

def render_linked_list(head) -> str:
    parts = []
    seen = set()
    node = head
    count = 0
    while node is not None:
        if id(node) in seen:
            parts.append("↺(cycle)")
            return " → ".join(parts)
        seen.add(id(node))
        parts.append(_node_val(node))
        node = _get(node, "next")
        count += 1
        if count > _MAX_NODES:
            parts.append("…")
            return " → ".join(parts)
    parts.append("None")
    return " → ".join(parts)


# ------------------------------------------------------------------------------
#  Binary trees:  compact 2D drawing
#
#         __4__
#        /     \
#       2       6
#      / \     / \
#     1   3   5   7
# ------------------------------------------------------------------------------

def render_tree(root) -> str:
    if root is None:
        return "(empty tree)"
    lines, *_ = _tree_lines(root, set())
    return "\n".join(lines)


def _tree_lines(node, seen):
    """Return (lines, width, height, middle) for the subtree rooted at `node`.

    `middle` is the horizontal index of this node's value within its block —
    used by the parent to center the connecting slashes.
    Algorithm adapted from the classic recursive ASCII binary-tree layout.
    """
    if id(node) in seen:
        s = "↺"
        return [s], len(s), 1, len(s) // 2
    seen = seen | {id(node)}

    label = _node_val(node)
    left = _get(node, "left")
    right = _get(node, "right")

    # Leaf.
    if left is None and right is None:
        return [label], len(label), 1, len(label) // 2

    # Only left child.
    if right is None:
        lines, n, p, x = _tree_lines(left, seen)
        first = (x + 1) * " " + (n - x - 1) * "_" + label
        second = x * " " + "/" + (n - x - 1 + len(label)) * " "
        shifted = [ln + len(label) * " " for ln in lines]
        return [first, second] + shifted, n + len(label), p + 2, n + len(label) // 2

    # Only right child.
    if left is None:
        lines, n, p, x = _tree_lines(right, seen)
        first = label + x * "_" + (n - x) * " "
        second = (len(label) + x) * " " + "\\" + (n - x - 1) * " "
        shifted = [len(label) * " " + ln for ln in lines]
        return [first, second] + shifted, n + len(label), p + 2, len(label) // 2

    # Two children.
    left_lines, ln, lp, lx = _tree_lines(left, seen)
    right_lines, rn, rp, rx = _tree_lines(right, seen)
    first = (lx + 1) * " " + (ln - lx - 1) * "_" + label + rx * "_" + (rn - rx) * " "
    second = (lx * " " + "/" + (ln - lx - 1 + len(label) + rx) * " " + "\\"
              + (rn - rx - 1) * " ")
    if lp < rp:
        left_lines += [ln * " "] * (rp - lp)
    elif rp < lp:
        right_lines += [rn * " "] * (lp - rp)
    zipped = [a + len(label) * " " + b for a, b in zip(left_lines, right_lines)]
    return ([first, second] + zipped,
            ln + rn + len(label),
            max(lp, rp) + 2,
            ln + len(label) // 2)


# ------------------------------------------------------------------------------
#  Entry point used by the engine's value formatter.
# ------------------------------------------------------------------------------

def render_value(value):
    """Return a string drawing for special structures, else None."""
    if is_tree_node(value):
        return "\n" + render_tree(value)
    if is_list_node(value):
        return render_linked_list(value)
    return None


# ------------------------------------------------------------------------------
#  Self-test:  python3 _viz.py
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    class LN:
        def __init__(self, v, nxt=None):
            self.value = v
            self.next = nxt

    class TN:
        def __init__(self, v, left=None, right=None):
            self.val = v
            self.left = left
            self.right = right

    ll = LN("Mario", LN("Luigi", LN("Wario", LN("Toad"))))
    print("Linked list:")
    print("  " + render_linked_list(ll))
    print()

    tree = TN(4, TN(2, TN(1), TN(3)), TN(6, TN(5), TN(7)))
    print("Balanced tree:")
    print(render_tree(tree))
    print()

    skew = TN(10, TN(5, TN(2), None), TN(20, None, TN(30)))
    print("Lopsided tree:")
    print(render_tree(skew))
