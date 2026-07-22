class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def middle_match(head, val):
    pass

# Input List:
# 1 -> 2 -> 3
# Input: head = 1, val = 2
_a3 = Node(3)
_a2 = Node(2, _a3)
_a1 = Node(1, _a2)
print(middle_match(_a1, 2))

# Input List:
# 1 -> 2 -> 3 -> 4
# Input: head = 1, val = 2
_b4 = Node(4)
_b3 = Node(3, _b4)
_b2 = Node(2, _b3)
_b1 = Node(1, _b2)
print(middle_match(_b1, 2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list, value matches")
single = Node(5)
print("  expected:", True, "| got:", middle_match(single, 5))

print("Test 2 - single-node list, value does not match")
single2 = Node(5)
print("  expected:", False, "| got:", middle_match(single2, 9))

print("Test 3 - two-node list, second (middle) node matches")
tw2 = Node('B')
tw1 = Node('A', tw2)
print("  expected:", True, "| got:", middle_match(tw1, 'B'))


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

grade(middle_match)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], 2, expected=True)   # checks the value your code returns against this example
