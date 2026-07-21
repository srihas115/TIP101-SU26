class Node:
    def __init__(self, value, next=None):
        self.value = value

        self.next = next


def rotate_right(head, k):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# num1 -> num2 -> num3 -> num4 -> num5
num5 = Node(5)
num4 = Node(4, num5)
num3 = Node(3, num4)
num2 = Node(2, num3)
num1 = Node(1, num2)
new_head = rotate_right(num1, 2)
print(_to_list(new_head))

# num1 -> num2 -> num3, k greater than list length
m3 = Node(3)
m2 = Node(2, m3)
m1 = Node(1, m2)
new_head2 = rotate_right(m1, 4)
print(_to_list(new_head2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node(9)
result1 = rotate_right(single, 3)
print("  expected:", [9], "| got:", _to_list(result1))

print("Test 2 - k is 0 (no rotation)")
z2 = Node('B')
z1 = Node('A', z2)
result2 = rotate_right(z1, 0)
print("  expected:", ['A', 'B'], "| got:", _to_list(result2))

print("Test 3 - k equals the list length (unchanged)")
e3 = Node(3)
e2 = Node(2, e3)
e1 = Node(1, e2)
result3 = rotate_right(e1, 3)
print("  expected:", [1, 2, 3], "| got:", _to_list(result3))
