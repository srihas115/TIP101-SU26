'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 2  ·  Version 3
  Problem 2: Where Does it Go (Iterative)

  Given a sorted array of distinct integers and a target value, return the
  index if the target is found. If not, return the index where it would be
  if it were inserted in order. You must write an algorithm with `O(log n)`
  runtime complexity.

  Write your solution for `search_insert` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `search_insert` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def search_insert(nums, target):
    pass

# Example Input: nums = [1, 3, 5, 7, 9, 11, 13, 15], target = 20


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

grade(search_insert)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 3, 5, 7, 9, 11, 13, 15], 20, expected=8)   # checks the value your code returns against this example
