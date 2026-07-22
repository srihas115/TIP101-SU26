'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 3
  Problem 1: Highest Exponent

  Write a function `find_highest_exponent()` that takes in an integer `base`
  and an integer `limit` as parameters. The function returns the highest
  exponent for which a given `base` raised to that exponent is less than or
  equal to `limit`.

  Write your solution for `find_highest_exponent` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_highest_exponent` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_highest_exponent(base, limit):
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

grade(find_highest_exponent)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(2, 100, expected=6)   # checks the value your code returns against this example
