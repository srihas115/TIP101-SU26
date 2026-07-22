'''
==============================================================================
  Unit 10: Review  ·  Session 2  ·  Version 3
  Problem 5: Custom Sort String

  You are given two strings `order` and `s`. All the characters of `order`
  are **unique** and were sorted in some custom order previously.

  Rearrange the characters of `s` so that they match the order that `order`
  was sorted. More specifically, if a character `x` occurs before a
  character `y` in `order`, then `x` should occur before `y` in the permuted
  string.

  Return *any permutation of* `s` *that satisfies this property*.

  Write your solution for `custom_sort_string` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `custom_sort_string` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def custom_sort_string(order, s):
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
from problem_set_solution_validator import grade

grade(custom_sort_string)   # ▶ Run this file to validate your solution
