class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def tail_to_head(head):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# Input: 1 -> 2 -> 3 -> 4
_n4 = Node(4)
_n3 = Node(3, _n4)
_n2 = Node(2, _n3)
_n1 = Node(1, _n2)
result = tail_to_head(_n1)
print(_to_list(result))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list (unchanged)")
single = Node(9)
result1 = tail_to_head(single)
print("  expected:", [9], "| got:", _to_list(result1))

print("Test 2 - two-node list (swaps the two nodes)")
t2 = Node('B')
t1 = Node('A', t2)
result2 = tail_to_head(t1)
print("  expected:", ['B', 'A'], "| got:", _to_list(result2))

print("Test 3 - list with duplicate values")
d3 = Node('x')
d2 = Node('y', d3)
d1 = Node('x', d2)
result3 = tail_to_head(d1)
print("  expected:", ['x', 'x', 'y'], "| got:", _to_list(result3))
