'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 1
  Problem 5: Restock Inventory

  Write a function `restock_inventory()` that updates an inventory
  dictionary based on a restock list. It accepts two parameters: -
  `current_inventory`: a dictionary where each key-value pair represents an
  item and its current stock in the inventory - `restock_list`: a dictionary
  where each key-value pair represents an item and the quantity to be added
  to the inventory

  If an item in `restock_list` is not present in the `current_inventory`, it
  should be added. The function should return the updated dictionary
  `current_inventory`.

  Write your solution for `restock_inventory` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `restock_inventory` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def restock_inventory(current_inventory, restock_list):
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

grade(restock_inventory)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'apples': 30, 'bananas': 15, 'oranges': 10}, {'oranges': 20, 'apples': 10, 'pears': 5}, expected={'apples': 40, 'bananas': 15, 'oranges': 30, 'pears': 5})   # checks the value your code returns against this example
