'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 2  ·  Version 1
  Problem 3: Binary Search IV

  Thus far, we’ve mostly been using an iterative implementation of the
  binary search algorithm. Recursive implementations of binary search are
  also very common. Implement `binary_search()` recursively.

  Write your solution for `binary_search` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `binary_search` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def binary_search(nums, target):
    pass

# Example Input: nums = [1, 3, 5, 7, 9, 11, 13, 15], target = 11


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

grade(binary_search)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 3, 5, 7, 9, 11, 13, 15], 11, expected=5)   # checks the value your code returns against this example
