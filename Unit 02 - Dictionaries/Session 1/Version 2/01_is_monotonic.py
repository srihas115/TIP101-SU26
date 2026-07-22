'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 2
  Problem 1: Is Monotonic

  Write a function `is_monotonic()` that takes in a list `nums` as a
  parameter and checks if it is either monotone increasing or monotone
  decreasing. A list is monotone increasing if every element is either
  greater than or equal to the element before it. A list is monotone
  decreasing if every element is either less than or equal to the element
  before it. The function should return `True` if the given list is either
  monotone increasing or decreasing and `False` otherwise. *Hint: This is a
  **lists** problem*

  Write your solution for `is_monotonic` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `is_monotonic` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def is_monotonic(nums):
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

grade(is_monotonic)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 2, 3, 10], expected=True)   # checks the value your code returns against this example
