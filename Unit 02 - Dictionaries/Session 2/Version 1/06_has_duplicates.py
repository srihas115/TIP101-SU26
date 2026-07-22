'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 1
  Problem 6: Has Duplicates

  Write a function `has_duplicates()` that takes in a list of integers
  `nums` and a positive number `k` as parameters. The function returns
  `True` if the list contains any duplicate elements within `k` (inclusive)
  indices of each other. In other words, return `True` if `nums[i]` has the
  same value as any of the `k` neighboring elements to its left or right. If
  `k` is greater than the list's length, the solution should check for
  duplicates in the complete list. The function should return `False`
  otherwise.

  Write your solution for `has_duplicates` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `has_duplicates` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def has_duplicates(nums, k):
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

grade(has_duplicates)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 6, 8, 2, 6, 4, 9], 2, expected=False)   # checks the value your code returns against this example
