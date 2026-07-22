class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next= next

def print_linked_list(head):
    pass

# input linked list: a->b->c->d->e
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.next = b
b.next = c
c.next = d
d.next = e
print_linked_list(a)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (head is None)")
print("  expected:", [], "| got:", print_linked_list(None))

print("Test 2 - single-node list")
single = Node('x')
print("  expected:", ['x'], "| got:", print_linked_list(single))

print("Test 3 - two-node list")
n1 = Node(1)
n2 = Node(2)
n1.next = n2
print("  expected:", [1, 2], "| got:", print_linked_list(n1))

print("Test 4 - list with duplicate values")
d1 = Node('z')
d2 = Node('z')
d3 = Node('z')
d1.next = d2
d2.next = d3
print("  expected:", ['z', 'z', 'z'], "| got:", print_linked_list(d1))


'''
==============================================================================
  PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import grade, test

grade(print_linked_list)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['a', 'b', 'c', 'd', 'e'], expected=['a', 'b', 'c', 'd', 'e'])   # checks the value your code returns against this example
