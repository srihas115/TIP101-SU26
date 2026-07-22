class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def has_cycle(head):
    pass

# Input List:
# 1 -> 2 -> 3 -> 4
#      ^         |
#      |---------|
# Input: head = 1
_n1 = Node(1)
_n2 = Node(2)
_n3 = Node(3)
_n4 = Node(4)
_n1.next = _n2
_n2.next = _n3
_n3.next = _n4
_n4.next = _n2  # cycle back to node 2
print(has_cycle(_n1))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - non-cyclic list (should NOT be falsely flagged as cyclic)")
nc3 = Node(3)
nc2 = Node(2, nc3)
nc1 = Node(1, nc2)
print("  expected:", False, "| got:", has_cycle(nc1))

print("Test 2 - single-node self-cycle")
self_node = Node(9)
self_node.next = self_node
print("  expected:", True, "| got:", has_cycle(self_node))

print("Test 3 - single-node list, no cycle")
single = Node(5)
print("  expected:", False, "| got:", has_cycle(single))

print("Test 4 - empty list (head is None)")
print("  expected:", False, "| got:", has_cycle(None))


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

grade(has_cycle)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([[1, 2, 3, 4], 1], expected=True)   # checks the value your code returns against this example
