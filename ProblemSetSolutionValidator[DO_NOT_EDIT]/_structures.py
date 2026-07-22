# ==============================================================================
#  PROBLEM SET SOLUTION VALIDATOR DATA STRUCTURES  —  DO NOT EDIT  ·  DO NOT DELETE
# ==============================================================================
#  Builders and converters that let the problem set solution validator grade functions which take or
#  return linked lists / binary trees. Inputs and answers are stored as plain
#  arrays; these helpers turn arrays into node structures before a call and back
#  into a canonical array after, so grading compares clean, comparable values.
#
#  Everything is duck-typed to the markdown's attribute names, so a student's own
#  Node / TreeNode class works without importing anything:
#     linked list node:  .value  (or .val / .data)   and  .next
#     tree node:         .val    (or .value / .data)  and  .left / .right
#
#  Pure standard library.
# ==============================================================================

import copy
from collections import deque

_MAX = 10000  # safety cap against cycles / runaway structures


class Node:
    """Linked-list node. Different problem sets name the payload `.value` or `.val`;
    we store `.value` and expose `.val` as an alias so student code written against
    either attribute works on the nodes the problem set solution validator builds."""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    @property
    def val(self):
        return self.value

    @val.setter
    def val(self, v):
        self.value = v


class DNode:
    """Doubly-linked node (matches the markdown's Node: value + prev + next)."""
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class TreeNode:
    """Binary-tree node (matches the markdown's TreeNode: val + left + right)."""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class KeyNode:
    """Key-sorted BST node (matches the markdown's TreeNode: key + val + children).
    Used by the BST insert/remove problems, which sort by .key."""
    def __init__(self, key, val=None, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------------------------------
#  Duck-typed accessors
# ------------------------------------------------------------------------------

def node_value(node):
    for attr in ("value", "val", "data", "key"):
        if hasattr(node, attr):
            return getattr(node, attr)
    return None


def _next(node):
    return getattr(node, "next", None)


def _left(node):
    return getattr(node, "left", None)


def _right(node):
    return getattr(node, "right", None)


# ------------------------------------------------------------------------------
#  Linked lists  (array  <->  node chain)
# ------------------------------------------------------------------------------

def build_linked_list(arr):
    head = None
    for v in reversed(list(arr)):
        head = Node(v, head)
    return head


def linked_list_to_array(head):
    out = []
    seen = set()
    node = head
    count = 0
    while node is not None and id(node) not in seen and count < _MAX:
        seen.add(id(node))
        out.append(node_value(node))
        node = _next(node)
        count += 1
    return out


# ------------------------------------------------------------------------------
#  Binary trees  (level-order array  <->  node tree)  — LeetCode-style
# ------------------------------------------------------------------------------

def build_tree(arr):
    arr = list(arr)
    if not arr or arr[0] is None:
        return None
    it = iter(arr)
    root = TreeNode(next(it))
    q = deque([root])
    while q:
        node = q.popleft()
        try:
            lv = next(it)
        except StopIteration:
            break
        if lv is not None:
            node.left = TreeNode(lv)
            q.append(node.left)
        try:
            rv = next(it)
        except StopIteration:
            break
        if rv is not None:
            node.right = TreeNode(rv)
            q.append(node.right)
    return root


def tree_to_array(root):
    if root is None:
        return []
    out = []
    q = deque([root])
    count = 0
    while q and count < _MAX:
        node = q.popleft()
        count += 1
        if node is None:
            out.append(None)
            continue
        out.append(node_value(node))
        q.append(_left(node))
        q.append(_right(node))
    while out and out[-1] is None:
        out.pop()
    return out


# ------------------------------------------------------------------------------
#  Convert inputs before a call, and outputs before comparison
# ------------------------------------------------------------------------------

def build_cyclic(spec):
    """spec = [array, pos]. Build a linked list; if pos is a valid index, link the
    tail's next back to the node at that index (creating a cycle)."""
    arr, pos = spec[0], spec[1]
    head = build_linked_list(arr)
    if pos is None or pos < 0 or head is None:
        return head
    node = head
    target = None
    idx = 0
    last = head
    while node is not None:
        if idx == pos:
            target = node
        last = node
        node = node.next
        idx += 1
    if target is not None:
        last.next = target
    return head


def build_circular(arr):
    """Build a linked list whose tail points back at the head (a circular list)."""
    head = build_linked_list(arr)
    if head is None:
        return None
    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = head
    return head


def build_doubly(arr):
    """Build a doubly-linked list (each node has .prev and .next)."""
    head = None
    prev = None
    for v in arr:
        node = DNode(v, prev, None)
        if prev is None:
            head = node
        else:
            prev.next = node
        prev = node
    return head


def build_single_node(value):
    """A single detached node holding one value (for e.g. add_first(head, new_node))."""
    return Node(value)


def build_circular_at(spec):
    """spec = [array, index]. Build a circular (tail->head) sorted list and return
    the node at `index` — for problems given a reference to any node in the ring.
    An empty array yields None."""
    arr = spec[0]
    idx = spec[1] if len(spec) > 1 else 0
    head = build_circular(arr)
    if head is None:
        return None
    node = head
    for _ in range(idx):
        node = node.next
    return node


def build_doubly_tail(arr):
    """Build a doubly-linked list and return its TAIL node (for print_reverse)."""
    head = build_doubly(arr)
    if head is None:
        return None
    node = head
    while node.next is not None:
        node = node.next
    return node


def build_doubly_at(spec):
    """spec = [array, index]. Build a doubly-linked list and return the node at
    `index` (for functions given a node at an unknown position)."""
    arr, idx = spec[0], spec[1]
    head = build_doubly(arr)
    node = head
    for _ in range(idx):
        node = node.next
    return node


# ------------------------------------------------------------------------------
#  Key-sorted binary search trees  (level-order key array <-> KeyNode tree)
# ------------------------------------------------------------------------------

def _node_key(node):
    for attr in ("key", "val", "value", "data"):
        if hasattr(node, attr):
            return getattr(node, attr)
    return None


def build_keytree(arr):
    """Level-order array of KEYS -> a KeyNode tree (val defaults to the key)."""
    arr = list(arr)
    if not arr or arr[0] is None:
        return None
    it = iter(arr)
    k0 = next(it)
    root = KeyNode(k0, k0)
    q = deque([root])
    while q:
        node = q.popleft()
        try:
            lk = next(it)
        except StopIteration:
            break
        if lk is not None:
            node.left = KeyNode(lk, lk)
            q.append(node.left)
        try:
            rk = next(it)
        except StopIteration:
            break
        if rk is not None:
            node.right = KeyNode(rk, rk)
            q.append(node.right)
    return root


def keytree_to_array(root):
    """A KeyNode tree -> a canonical level-order array of KEYS."""
    if root is None:
        return []
    out = []
    q = deque([root])
    count = 0
    while q and count < _MAX:
        node = q.popleft()
        count += 1
        if node is None:
            out.append(None)
            continue
        out.append(_node_key(node))
        q.append(_left(node))
        q.append(_right(node))
    while out and out[-1] is None:
        out.pop()
    return out


def find_by_key(root, key):
    """Locate the node in a tree whose key/val matches (for node-reference args)."""
    q = deque([root])
    count = 0
    while q and count < _MAX:
        node = q.popleft()
        count += 1
        if node is None:
            continue
        if _node_key(node) == key:
            return node
        q.append(_left(node))
        q.append(_right(node))
    return None


def find_by_val(root, value):
    """Locate the node in a value tree whose .val matches (for node-reference args)."""
    q = deque([root])
    count = 0
    while q and count < _MAX:
        node = q.popleft()
        count += 1
        if node is None:
            continue
        if node_value(node) == value:
            return node
        q.append(_left(node))
        q.append(_right(node))
    return None


def _canon_node_key(node):
    """A returned BST node (or None) -> its key (or None)."""
    if node is None:
        return None
    return _node_key(node)


def _canon_node_value(value):
    """Accept either a returned node OR a raw value — return the value either way."""
    if hasattr(value, "value") or hasattr(value, "val") or hasattr(value, "data"):
        return node_value(value)
    return value


def _canon_node_value_list(value):
    """A returned list of nodes (or values) -> a plain list of their values."""
    if value is None:
        return []
    return [_canon_node_value(n) for n in value]


def doubly_to_array(head):
    """Walk a doubly-linked list forward into [values, prev_pointers_consistent].
    The second element flags whether every node's .prev points back correctly, so
    a solution that fixes .next but forgets .prev is caught."""
    vals = []
    prev_ok = True
    seen = set()
    expected_prev = None
    node = head
    count = 0
    while node is not None and id(node) not in seen and count < _MAX:
        seen.add(id(node))
        vals.append(node_value(node))
        if getattr(node, "prev", None) is not expected_prev:
            prev_ok = False
        expected_prev = node
        node = _next(node)
        count += 1
    return [vals, prev_ok]


_BUILDERS = {"linkedlist": build_linked_list, "tree": build_tree, "cyclic": build_cyclic,
             "circular": build_circular, "doubly": build_doubly, "keytree": build_keytree,
             "node": build_single_node, "doubly_tail": build_doubly_tail,
             "doubly_at": build_doubly_at, "circular_at": build_circular_at}
_CANON = {"linkedlist": linked_list_to_array, "tree": tree_to_array,
          "node_value": _canon_node_value, "node_value_list": _canon_node_value_list,
          "doubly": doubly_to_array, "keytree": keytree_to_array,
          "node_key": _canon_node_key}


def prepare_args(args, arg_kinds):
    """Turn stored array args into node structures where arg_kinds says so.
    The special kind "node_by_key" resolves to the node inside the FIRST built
    argument (the tree/root) whose key matches — used for problems that take a
    reference to an existing node, like inorder_successor(root, current)."""
    if not arg_kinds:
        return list(args)
    out = []
    for i, a in enumerate(args):
        kind = arg_kinds[i] if i < len(arg_kinds) else "plain"
        if kind == "node_by_key":
            out.append(find_by_key(out[0], a))
        elif kind == "node_by_val":
            out.append(find_by_val(out[0], a))
        elif kind == "clone_prev":
            # a deep copy of the FIRST built argument (its stored value is ignored);
            # used for "cloned tree" problems like get_target_copy(original, cloned, ...)
            out.append(copy.deepcopy(out[0]))
        elif kind in _BUILDERS:
            out.append(_BUILDERS[kind](a))
        else:
            out.append(a)
    return out


def canon(value, ret_kind):
    """Turn a returned structure into a canonical array for comparison."""
    return _CANON[ret_kind](value) if ret_kind in _CANON else value


# ------------------------------------------------------------------------------
#  Pretty rendering for feedback (arrays -> arrows / ASCII tree)
# ------------------------------------------------------------------------------

def render_canon(value, kind):
    """Render a canonical array back into a readable structure for feedback."""
    try:
        if kind == "linkedlist":
            from _viz import render_linked_list
            return render_linked_list(build_linked_list(value)) if value else "None (empty list)"
        if kind in ("tree", "keytree"):
            from _viz import render_tree
            return "\n" + render_tree(build_tree(value)) if value else "(empty tree)"
        if kind == "doubly":
            vals, prev_ok = (value if value else [[], True])
            if not vals:
                return "None (empty list)"
            chain = " <-> ".join(str(v) for v in vals)
            return chain if prev_ok else chain + "   (⚠ some .prev pointers are wrong)"
    except Exception:
        pass
    return repr(value)
