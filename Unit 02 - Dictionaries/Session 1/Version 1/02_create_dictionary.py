'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 1
  Problem 2: Create a Dictionary

  Write a function `create_dictionary()` that takes in a list of `keys` and
  a list of `values` as parameters. The function returns a dictionary where
  each item in `keys` is paired with a corresponding item in `values`.

  `keys[i]` should be paired with `values[i]` in the dictionary where `0` <=
  `i` <= `len(keys)`. You may assume `keys` and `values` are the same
  length.

  Write your solution for `create_dictionary` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `create_dictionary` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def create_dictionary(keys, values):
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

grade(create_dictionary)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['peanut', 'dragon', 'star', 'pop', 'space'], ['butter', 'fly', 'fish', 'corn', 'ship'], expected={'peanut': 'butter', 'dragon': 'fly', 'star': 'fish', 'pop': 'corn', 'space': 'ship'})   # checks the value your code returns against this example
