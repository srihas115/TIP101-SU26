'''
==============================================================================
  Unit 10: Review  ·  Session 1  ·  Version 2
  Problem 1: Flowerbed

  You have a long flowerbed in which some of the plots are planted, and some
  are not. However, flowers cannot be planted in **adjacent** plots.

  Given a list of integers `flowerbed` containing `0`'s and `1`'s, where `0`
  means empty and `1` means not empty, and an integer `n`, return `True`
  *if* `n` *new flowers can be planted in the* `flowerbed` *without
  violating the no-adjacent-flowers rule and* `False` *otherwise*.

  Write your solution for `can_place_flowers` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `can_place_flowers` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def can_place_flowers(flowerbed, n):
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

grade(can_place_flowers)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 0, 0, 0, 1], 1, expected=True)   # checks the value your code returns against this example
