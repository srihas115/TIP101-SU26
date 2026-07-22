'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 2
  Problem 6: Two-Pointer Remove Element

  The two-pointer approach can also be used with two pointers that iterate
  forward through a list or string at different rates. Use two pointers to
  solve the following problem:

  Write a function `remove_element()` that takes in a list `nums` and a
  value `val` as parameters and removes all instances of that value in-
  place. The function returns the new length of `nums`.

  Write your solution for `remove_element` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `remove_element` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def remove_element(nums, val):
    pass

nums = [5, 4, 4, 3, 4, 1]
nums_len = remove_element(nums, 4)
print(nums) # same list
print(nums_len)


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

grade(remove_element)   # ▶ Run this file to validate your solution
