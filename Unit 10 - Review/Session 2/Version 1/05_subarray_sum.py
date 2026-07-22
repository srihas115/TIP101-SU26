'''
==============================================================================
  Unit 10: Review  ·  Session 2  ·  Version 1
  Problem 5: Subarray Sum Equals K

  Given an array of integers `nums` and an integer `k`, return *the total
  number of subarrays whose sum equals to* `k`.

  A subarray is a contiguous **non-empty** sequence of elements within an
  array.

  Write your solution for `subarray_sum` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `subarray_sum` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def subarray_sum(nums, k):
    pass


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

grade(subarray_sum)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 1, 1], 2, expected=2)   # checks the value your code returns against this example
