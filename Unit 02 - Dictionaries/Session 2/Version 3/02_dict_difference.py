'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 3
  Problem 2: Dictionary Difference

  Write a function `dict_difference()` that takes two dictionaries and
  returns a new dictionary that contains only the key-value pairs found only
  in the first dictionary but not in the second.

  Write your solution for `dict_difference` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `dict_difference` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def dict_difference(d1, d2):
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

grade(dict_difference)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'b': 2, 'd': 1}, expected={'a': 1, 'c': 3, 'd': 4})   # checks the value your code returns against this example
