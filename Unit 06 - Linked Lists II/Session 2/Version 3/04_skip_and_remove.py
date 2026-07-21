class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def skip_and_remove(head, m, n):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, m = 2, n = 3
_v = list(range(1, 11))
_nodes = [Node(x) for x in _v]
for _i in range(len(_nodes) - 1):
    _nodes[_i].next = _nodes[_i + 1]
result = skip_and_remove(_nodes[0], 2, 3)
print(_to_list(result))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - m equals the full list length (nothing removed)")
w3 = Node(3)
w2 = Node(2, w3)
w1 = Node(1, w2)
result1 = skip_and_remove(w1, 10, 3)
print("  expected:", [1, 2, 3], "| got:", _to_list(result1))

print("Test 2 - n larger than remaining nodes (last partial group all removed)")
x5 = Node(5)
x4 = Node(4, x5)
x3 = Node(3, x4)
x2 = Node(2, x3)
x1 = Node(1, x2)
result2 = skip_and_remove(x1, 2, 10)
print("  expected:", [1, 2], "| got:", _to_list(result2))

print("Test 3 - single-node list, m keeps it")
single = Node(9)
result3 = skip_and_remove(single, 1, 2)
print("  expected:", [9], "| got:", _to_list(result3))
