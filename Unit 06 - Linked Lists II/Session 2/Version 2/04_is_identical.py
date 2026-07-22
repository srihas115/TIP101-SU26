'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 2  ·  Version 2
  Problem 4: Identical Linked Lists

  Two linked lists are identical when they have the same values and the same
  order of values. Given the heads of two linked lists, write a function
  that returns `True` if the the linked lists are identical and `False`
  otherwise.

  Write your solution for `is_identical` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `is_identical` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_identical(head_a, head_b):
    pass

# list1: 1->2->3->4
# list2: 1->2->3->4
# head_a = 1, head_b = 1,
_a4 = Node(4)
_a3 = Node(3, _a4)
_a2 = Node(2, _a3)
head_a = Node(1, _a2)

_b4 = Node(4)
_b3 = Node(3, _b4)
_b2 = Node(2, _b3)
head_b = Node(1, _b2)
print(is_identical(head_a, head_b))

# list1: 1->2->3->4
# list2: 1->3->4->2
_c4 = Node(2)
_c3 = Node(4, _c4)
_c2 = Node(3, _c3)
head_c = Node(1, _c2)
print(is_identical(head_a, head_c))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - both empty lists (identical)")
print("  expected:", True, "| got:", is_identical(None, None))

print("Test 2 - one empty, one non-empty")
single = Node(1)
print("  expected:", False, "| got:", is_identical(None, single))

print("Test 3 - single-node lists, same value")
s1 = Node(5)
s2 = Node(5)
print("  expected:", True, "| got:", is_identical(s1, s2))

print("Test 4 - different lengths")
d2 = Node(2)
d1 = Node(1, d2)
print("  expected:", False, "| got:", is_identical(d1, s1))


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

grade(is_identical)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4], [1, 2, 3, 4], expected=True)   # checks the value your code returns against this example
