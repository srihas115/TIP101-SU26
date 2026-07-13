class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_dupes(head):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# Example Input: 1 -> 2 -> 3 -> 3 -> 4 -> 5
_v = [1, 2, 3, 3, 4, 5]
_nodes = [Node(x) for x in _v]
for _i in range(len(_nodes) - 1):
    _nodes[_i].next = _nodes[_i + 1]
result = delete_dupes(_nodes[0])
print(_to_list(result))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (head is None)")
print("  expected:", [], "| got:", _to_list(delete_dupes(None)))

print("Test 2 - single-node list (unchanged)")
single = Node(9)
print("  expected:", [9], "| got:", _to_list(delete_dupes(single)))

print("Test 3 - all elements are duplicates (result is empty)")
a2 = Node(1)
a1 = Node(1, a2)
print("  expected:", [], "| got:", _to_list(delete_dupes(a1)))

print("Test 4 - multiple separate duplicate groups")
b5 = Node(5)
b4 = Node(4, b5)
b3 = Node(2, b4)
b2 = Node(1, b3)
b1 = Node(1, b2)
print("  expected:", [2, 4, 5], "| got:", _to_list(delete_dupes(b1)))
