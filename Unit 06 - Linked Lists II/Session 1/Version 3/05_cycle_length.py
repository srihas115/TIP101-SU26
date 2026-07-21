class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def cycle_length(head):
    pass

# Input List
# 1 -> 2 -> 3 -> 4
#      ^         |
#      |_________|
# Input: head = 1
_n1 = Node(1)
_n2 = Node(2)
_n3 = Node(3)
_n4 = Node(4)
_n1.next = _n2
_n2.next = _n3
_n3.next = _n4
_n4.next = _n2  # cycle back to node 2
print(cycle_length(_n1))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - non-cyclic list (no cycle, length 0)")
nc3 = Node(3)
nc2 = Node(2, nc3)
nc1 = Node(1, nc2)
print("  expected:", 0, "| got:", cycle_length(nc1))

print("Test 2 - single-node self-cycle (cycle length 1)")
self_node = Node(9)
self_node.next = self_node
print("  expected:", 1, "| got:", cycle_length(self_node))

print("Test 3 - entire list is the cycle (cycle length equals list length)")
c1 = Node('a')
c2 = Node('b')
c3 = Node('c')
c1.next = c2
c2.next = c3
c3.next = c1
print("  expected:", 3, "| got:", cycle_length(c1))
