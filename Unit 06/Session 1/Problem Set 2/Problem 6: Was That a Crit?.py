class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def count_critical_points(head):
    pass

# Input List: 1 -> 2 -> 3 -> 3 -> 3 -> 5 -> 1 -> 3
_v = [1, 2, 3, 3, 3, 5, 1, 3]
_nodes = [Node(x) for x in _v]
for _i in range(len(_nodes) - 1):
    _nodes[_i].next = _nodes[_i + 1]
print(count_critical_points(_nodes[0]))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list (no critical points possible)")
single = Node(5)
print("  expected:", 0, "| got:", count_critical_points(single))

print("Test 2 - two-node list (no critical points possible)")
tw2 = Node(2)
tw1 = Node(1, tw2)
print("  expected:", 0, "| got:", count_critical_points(tw1))

print("Test 3 - all elements the same (no strict minima/maxima)")
same3 = Node(4)
same2 = Node(4, same3)
same1 = Node(4, same2)
print("  expected:", 0, "| got:", count_critical_points(same1))
