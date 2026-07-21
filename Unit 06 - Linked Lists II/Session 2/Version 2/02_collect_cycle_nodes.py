class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_cycle_nodes(head):
    pass

# num1 -> num2 -> num3 -> num4 -> num2
num4 = Node(4)
num3 = Node(3, num4)
num2 = Node(2, num3)
num1 = Node(1, num2)
num4.next = num2  # cycle back to num2
lst = collect_cycle_nodes(num1)
print([n.value for n in lst] if lst else [])

# var1 -> var2 -> var3 -> var4
var4 = Node(4)
var3 = Node(3, var4)
var2 = Node(2, var3)
var1 = Node(1, var2)
lst2 = collect_cycle_nodes(var1)
print([n.value for n in lst2] if lst2 else [])

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node self-cycle")
self_node = Node(9)
self_node.next = self_node
result1 = collect_cycle_nodes(self_node)
print("  expected:", [9], "| got:", [n.value for n in result1] if result1 else [])

print("Test 2 - empty list (head is None)")
result2 = collect_cycle_nodes(None)
print("  expected:", [], "| got:", [n.value for n in result2] if result2 else [])
