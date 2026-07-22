'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 2
  Problem 6: How Many Smaller

  Write a function `smaller_numbers_than_current()` that takes in a list of
  numbers `nums` as a parameter. For each `nums[i]`, the function should
  find out how many numbers in the list are smaller than it. (*For each
  nums[i], count the number of valid `j`'s such that `j!=i` and `nums[j] <
  nums[i]`*)

  Return the answers in a list.

  Write your solution for `smaller_numbers_than_current` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `smaller_numbers_than_current` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def smaller_numbers_than_current(nums):
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

grade(smaller_numbers_than_current)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([6, 1, 2, 2, 3], expected=[4, 0, 1, 1, 3])   # checks the value your code returns against this example
