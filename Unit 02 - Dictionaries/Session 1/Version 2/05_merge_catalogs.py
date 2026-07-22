'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 2
  Problem 5: Merge Catalogs

  Write a function `merge_catalogs()` that combines two product catalogs,
  `catalog1` and `catalog2` as parameters. Each parameter is a dictionary
  where each key-value pair represents a product name and its price,
  respectively. If the same product exists in both catalogs, the price from
  the second catalog should overwrite the price in the first. Return the
  updated first catalog dictionary.

  Write your solution for `merge_catalogs` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `merge_catalogs` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def merge_catalogs(catalog1, catalog2):
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

grade(merge_catalogs)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'apple': 1.0, 'banana': 0.5}, {'banana': 0.75, 'cherry': 1.25}, expected={'apple': 1.0, 'banana': 0.75, 'cherry': 1.25})   # checks the value your code returns against this example
