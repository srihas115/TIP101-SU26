'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 3
  Problem 8: First Unique Items

  Write a function `find_unique_items()` that takes two lists `list_a` and
  `list_b` as parameters. The function identifies unique items from the
  lists and returns a dictionary with the items as keys and a boolean value
  as the value indicating whether the item is unique to the first list
  (`True`) or not (`False`).

  Write your solution for `find_unique_items` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_unique_items` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_unique_items(list_a, list_b):
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

grade(find_unique_items)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['apple', 'banana', 'carrot'], ['apple', 'banana', 'date'], expected={'date': False, 'carrot': True})   # checks the value your code returns against this example
