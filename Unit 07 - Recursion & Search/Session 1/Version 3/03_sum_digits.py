'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 1  ·  Version 3
  Problem 3: Recursive Digits Sum

  Given a non-negative integer n, write a function `sum_digits()` that
  calculates and returns the sum of its digits recursively.

  Evaluate the time and space complexity of your solution.

  Write your solution for `sum_digits` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `sum_digits` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def sum_digits(n):
    pass

# Example Input: 523


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

grade(sum_digits)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(523, expected=10)   # checks the value your code returns against this example
