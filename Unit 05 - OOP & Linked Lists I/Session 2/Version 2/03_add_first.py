class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def add_first(head, val):
    pass

# Linked List: A -> B -> C
node_c = Node('C')
node_b = Node('B', node_c)
node_a = Node('A', node_b)
new_list = add_first(node_a, 0)
# New List: 0 -> A -> B -> C

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

print(_to_list(new_list))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (head is None)")
result1 = add_first(None, 99)
print("  expected:", [99], "| got:", _to_list(result1))

print("Test 2 - single-node list")
single = Node('X')
result2 = add_first(single, 'Y')
print("  expected:", ['Y', 'X'], "| got:", _to_list(result2))

print("Test 3 - longer list, chain preserved")
result3 = add_first(node_a, -1)
print("  expected:", [-1, 'A', 'B', 'C'], "| got:", _to_list(result3))
