'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 3
  Problem 2: Build Inventory

  Write a function `build_inventory()` that takes in a list of
  `product_names` and a corresponding list of `product_prices` as
  parameters. The function returns a dictionary representing the inventory
  of a small store. Each product name in `product_names` should be a key in
  the dictionary and the corresponding value should be the item price.

  `product_names[i]` should be paired with `product_prices[i]` in the
  dictionary where `0` <= `i` <= `len(product_names)`. You may assume that
  `product_names` and `product_prices` are the same length.

  Write your solution for `build_inventory` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `build_inventory` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def build_inventory(product_names, product_prices):
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

grade(build_inventory)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['Apple', 'Banana', 'Orange'], [0.99, 0.5, 0.75], expected={'Apple': 0.99, 'Banana': 0.5, 'Orange': 0.75})   # checks the value your code returns against this example
