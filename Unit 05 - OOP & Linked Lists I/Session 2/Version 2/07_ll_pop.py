class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def ll_pop(head, i):
    pass

# linked list: num1 -> num2 -> num3
num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
new_head = ll_pop(num1, 1)
# result: num1 -> num3

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

print(_to_list(new_head))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - pop index 0 (removes the head)")
p3 = Node(3)
p2 = Node(2, p3)
p1 = Node(1, p2)
result1 = ll_pop(p1, 0)
print("  expected:", [2, 3], "| got:", _to_list(result1))

print("Test 2 - index greater than length (does nothing)")
q2 = Node(2)
q1 = Node(1, q2)
result2 = ll_pop(q1, 10)
print("  expected:", [1, 2], "| got:", _to_list(result2))

print("Test 3 - single-node list, pop index 0 (empties the list)")
s1 = Node(9)
result3 = ll_pop(s1, 0)
print("  expected:", [], "| got:", _to_list(result3))
