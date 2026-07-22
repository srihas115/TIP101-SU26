'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 2
  Problem 3: Sort List by Parity

  Write a function `sort_array_by_parity()` that takes in a list of integers
  `nums` where half of the integers are odd, and the other half are even.
  The function sorts the list so that whenever `nums[i]` is odd, `i` is odd
  and whenever `nums[i]` is even, `i` is even. The function returns the list
  in any order that satisfies the condition.

  Write your solution for `sort_array_by_parity` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `sort_array_by_parity` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def sort_array_by_parity(nums):
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
from problem_set_solution_validator import grade

grade(sort_array_by_parity)   # ▶ Run this file to validate your solution
