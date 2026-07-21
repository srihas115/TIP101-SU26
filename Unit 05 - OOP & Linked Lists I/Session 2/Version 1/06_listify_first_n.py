class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def listify_first_n(head, n):
    pass

# linked list: a -> b -> c
a = Node('a')
b = Node('b')
c = Node('c')
a.next = b
b.next = c
head = a
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l
j = Node('j')
k = Node('k')
l = Node('l')
j.next = k
k.next = l
head2 = j
lst2 = listify_first_n(head2,5)
print(lst2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (head is None)")
print("  expected:", [], "| got:", listify_first_n(None, 3))

print("Test 2 - n is 0")
print("  expected:", [], "| got:", listify_first_n(a, 0))

print("Test 3 - single-node list")
single = Node('x')
print("  expected:", ['x'], "| got:", listify_first_n(single, 1))

print("Test 4 - n exactly equals the list length")
print("  expected:", ['a', 'b', 'c'], "| got:", listify_first_n(a, 3))
