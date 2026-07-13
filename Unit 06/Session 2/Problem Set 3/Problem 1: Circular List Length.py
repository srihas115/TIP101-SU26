class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def circular_list_length(head):
    pass

# Input List: 1 -> 2 -> 3 -> 1 (circular)
c3 = Node(3)
c2 = Node(2, c3)
c1 = Node(1, c2)
c3.next = c1
print(circular_list_length(c1))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node circular list (self-loop)")
self_node = Node(9)
self_node.next = self_node
print("  expected:", 1, "| got:", circular_list_length(self_node))

print("Test 2 - longer circular list")
d5 = Node(5)
d4 = Node(4, d5)
d3 = Node(3, d4)
d2 = Node(2, d3)
d1 = Node(1, d2)
d5.next = d1
print("  expected:", 5, "| got:", circular_list_length(d1))
