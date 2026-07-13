class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def copy_ll(head):
    pass

# Linked List: 5 -> 6 -> 7
_c3 = Node(7)
_c2 = Node(6, _c3)
head = Node(5, _c2)
copy = copy_ll(head) # Linked List Copy: 5 -> 6 -> 7
print(head.value, copy.value)

# Change original list -- should not affect the copy
head.value = 10
print(head.value, copy.value)

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node(1)
copy1 = copy_ll(single)
print("  expected:", [1], "| got:", _to_list(copy1))

print("Test 2 - copy is a separate object, not the same node")
print("  expected:", True, "| got:", copy1 is not single)

print("Test 3 - list with duplicate values")
d2 = Node('x')
d1 = Node('x', d2)
copy3 = copy_ll(d1)
print("  expected:", ['x', 'x'], "| got:", _to_list(copy3))
