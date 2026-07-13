class Node:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

def print_reverse(tail):
    pass

#              (head)                       (tail)
# Linked List: Poliwag <-> Poliwhirl <-> Poliwrath
poliwag = Node("Poliwag")
poliwhirl = Node("Poliwhirl", prev=poliwag)
poliwag.next = poliwhirl
poliwrath = Node("Poliwrath", prev=poliwhirl)
poliwhirl.next = poliwrath
print_reverse(poliwrath)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node("Alone")
print("  expected printed output: Alone")
print_reverse(single)

print("Test 2 - two-node list")
tn1 = Node("A")
tn2 = Node("B", prev=tn1)
tn1.next = tn2
print("  expected printed output: B A")
print_reverse(tn2)

print("Test 3 - list with duplicate values")
d1 = Node("X")
d2 = Node("X", prev=d1)
d1.next = d2
d3 = Node("X", prev=d2)
d2.next = d3
print("  expected printed output: X X X")
print_reverse(d3)
