'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 1
  Problem 4: Positive Negative Pairs

  Write a function `find_largest_k()` that takes in a list of integers
  `nums` that does not contain any zeroes as a parameter. The function finds
  the **largest positive** integer `k` such that `-k` also exists in the
  array and returns `k`. If there is no such integer, return `-1`.

  Write your solution for `find_largest_k` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_largest_k` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_largest_k(nums):
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

grade(find_largest_k)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([-1, 2, -3, 3, -1], expected=3)   # checks the value your code returns against this example
