class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_min(head):
    pass

# Linked List: 5 -> 6 -> 7 -> 8
_a4 = Node(8)
_a3 = Node(7, _a4)
_a2 = Node(6, _a3)
_a1 = Node(5, _a2)
print(find_min(_a1))

# Linked List: 8 -> 5 -> 6 -> 7
_b4 = Node(7)
_b3 = Node(6, _b4)
_b2 = Node(5, _b3)
_b1 = Node(8, _b2)
print(find_min(_b1))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node(42)
print("  expected:", 42, "| got:", find_min(single))

print("Test 2 - all negative numbers")
n2 = Node(-1)
n1 = Node(-5, n2)
print("  expected:", -5, "| got:", find_min(n1))

print("Test 3 - duplicate minimum values")
m3 = Node(2)
m2 = Node(1, m3)
m1 = Node(1, m2)
print("  expected:", 1, "| got:", find_min(m1))


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

grade(find_min)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 6, 7, 8], expected=5)   # checks the value your code returns against this example
