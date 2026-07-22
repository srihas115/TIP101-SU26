'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 1  ·  Version 2
  Problem 11: Length of List

  Without using the built-in `len()` function, write a function
  `list_length()` that takes in a list `lst` as a parameter and returns the
  length of the list.

  Write your solution for `list_length` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `list_length` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def list_length(lst):
    l = 0
    for num in lst:
        l += 1
    return l

lst = [2,4,6,8,10]
length = list_length(lst)
print(length)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", 0, "| got:", list_length([]))

print("Test 2 - single-element list")
print("  expected:", 1, "| got:", list_length([9]))

print("Test 3 - list with duplicate values")
print("  expected:", 4, "| got:", list_length([2,2,2,2]))

print("Test 4 - larger list")
print("  expected:", 6, "| got:", list_length([1,2,3,4,5,6]))


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

grade(list_length)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([2, 4, 6, 8, 10], expected=5)   # checks the value your code returns against this example
