class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_second(head, val):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# linked list: 1 -> 3 -> 4
n1 = Node(1)
n3 = Node(3)
n4 = Node(4)
n1.next = n3
n3.next = n4
result = add_second(n1, 2)
print(_to_list(result))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list (new node becomes the second)")
single = Node('a')
result1 = add_second(single, 'b')
print("  expected:", ['a', 'b'], "| got:", _to_list(result1))

print("Test 2 - two-node list")
t2 = Node('y')
t1 = Node('x', t2)
result2 = add_second(t1, 'z')
print("  expected:", ['x', 'z', 'y'], "| got:", _to_list(result2))

print("Test 3 - list with duplicate values")
dup2 = Node('same')
dup1 = Node('same', dup2)
result3 = add_second(dup1, 'same')
print("  expected:", ['same', 'same', 'same'], "| got:", _to_list(result3))
