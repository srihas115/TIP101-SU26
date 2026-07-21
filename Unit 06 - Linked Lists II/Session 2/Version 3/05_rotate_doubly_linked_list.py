class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

def rotate_doubly_linked_list(head, k):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# Input List: 1 <-> 2 <-> 3 <-> 4 <-> 5, k = 2
_n5 = Node(5)
_n4 = Node(4, next=_n5)
_n5.prev = _n4
_n3 = Node(3, next=_n4)
_n4.prev = _n3
_n2 = Node(2, next=_n3)
_n3.prev = _n2
_n1 = Node(1, next=_n2)
_n2.prev = _n1
result = rotate_doubly_linked_list(_n1, 2)
print(_to_list(result))

# Input List: 0 <-> 1 <-> 2, k = 4 (wraps around)
_m2 = Node(2)
_m1 = Node(1, next=_m2)
_m2.prev = _m1
_m0 = Node(0, next=_m1)
_m1.prev = _m0
result2 = rotate_doubly_linked_list(_m0, 4)
print(_to_list(result2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node(9)
result3 = rotate_doubly_linked_list(single, 5)
print("  expected:", [9], "| got:", _to_list(result3))

print("Test 2 - k is 0 (no rotation)")
z2 = Node('B')
z1 = Node('A', next=z2)
z2.prev = z1
result4 = rotate_doubly_linked_list(z1, 0)
print("  expected:", ['A', 'B'], "| got:", _to_list(result4))

print("Test 3 - k equals the list length (unchanged)")
e3 = Node(3)
e2 = Node(2, next=e3)
e3.prev = e2
e1 = Node(1, next=e2)
e2.prev = e1
result5 = rotate_doubly_linked_list(e1, 3)
print("  expected:", [1, 2, 3], "| got:", _to_list(result5))
