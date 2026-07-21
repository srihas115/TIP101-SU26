class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_between(head, m, n):
    pass

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

# input list: 1 -> 2 -> 3 -> 4 -> 5
_n5 = Node(5)
_n4 = Node(4, _n5)
_n3 = Node(3, _n4)
_n2 = Node(2, _n3)
head = Node(1, _n2)
result = reverse_between(head, 2, 5)
print(_to_list(result))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - m equals n (no visible change)")
s5 = Node(5)
s4 = Node(4, s5)
s3 = Node(3, s4)
s2 = Node(2, s3)
s1 = Node(1, s2)
result1 = reverse_between(s1, 3, 3)
print("  expected:", [1, 2, 3, 4, 5], "| got:", _to_list(result1))

print("Test 2 - reverse the entire list (m=1, n=length)")
t3 = Node(3)
t2 = Node(2, t3)
t1 = Node(1, t2)
result2 = reverse_between(t1, 1, 3)
print("  expected:", [3, 2, 1], "| got:", _to_list(result2))

print("Test 3 - reverse a middle sublist not touching either end")
u5 = Node(5)
u4 = Node(4, u5)
u3 = Node(3, u4)
u2 = Node(2, u3)
u1 = Node(1, u2)
result3 = reverse_between(u1, 2, 4)
print("  expected:", [1, 4, 3, 2, 5], "| got:", _to_list(result3))
