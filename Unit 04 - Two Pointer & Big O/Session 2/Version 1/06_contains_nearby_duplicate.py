'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 1
  Problem 6: Duplicates Within Range

  Write a function `contains_nearby_duplicate()` that takes in a list `lst`
  and a positive number `k` as parameters. The function returns `True` if
  the list contains any duplicate elements within the range `k` and `False`
  otherwise. If `k` is more than the list's size, the solution should check
  for duplicates in the complete list.

  Write your solution for `contains_nearby_duplicate` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `contains_nearby_duplicate` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def contains_nearby_duplicate(lst, k):
    pass  # replace this line with your solution













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

grade(contains_nearby_duplicate)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 1, 2, 3], 2, expected=False)   # checks the value your code returns against this example
