class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def chase_list(head):
    pass

dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list (no 'chases' separator needed)")
single = Node("Spike")
print("  expected:", "Spike", "| got:", chase_list(single))

print("Test 2 - two-node list")
n1 = Node("A")
n2 = Node("B")
n1.next = n2
print("  expected:", "A chases B", "| got:", chase_list(n1))

print("Test 3 - empty list (head is None)")
print("  expected:", "", "| got:", chase_list(None))

print("Test 4 - list with duplicate values")
d1 = Node("X")
d2 = Node("X")
d3 = Node("X")
d1.next = d2
d2.next = d3
print("  expected:", "X chases X chases X", "| got:", chase_list(d1))
