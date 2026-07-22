'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 1  ·  Version 1
  Problem 7: Find Floor

  Given a sorted list of integers and a value `x`, return the index of the
  floor of `x`. The floor of `x` is the largest element in the array smaller
  than or equal to `x`. If there is no floor of `x`, return `-1`.

  Evaluate the time and space complexity of your function.

  Write your solution for `find_floor` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_floor` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_floor(lst, x):
    pass

# Example Input: lst = [1, 2, 8, 10, 11, 12, 19], x = 5


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

grade(find_floor)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 8, 10, 11, 12, 19], 5, expected=1)   # checks the value your code returns against this example
