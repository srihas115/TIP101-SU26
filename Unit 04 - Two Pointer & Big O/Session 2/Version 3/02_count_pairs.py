'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 3
  Problem 2: Count Pairs

  Write a function `count_pairs()` that takes in a *0-indexed* list of
  integers `nums` of length `n` and an integer `target` as parameters. The
  function returns the number of index pairs `(i, j)` where `0 <= i < j < n`
  and `nums[i] + nums[j] < target`.

  Write your solution for `count_pairs` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `count_pairs` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def count_pairs(nums, target):
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

grade(count_pairs)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([-1, 1, 2, 3, 1], 2, expected=3)   # checks the value your code returns against this example
