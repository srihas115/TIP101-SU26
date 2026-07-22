'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 3
  Problem 3: Take from Stock

  Write a function `pop_stock()` that takes a dictionary of items `items`
  that keeps track of an item and its stock quantity, an `item_name`, and a
  `quantity` to be removed as parameters. The function should remove the
  specified `quantity` for that item. If the item does not exist, return the
  string `"Item does not exist."` If the specified quantity is greater than
  the stock, return a string `"Not enough stock."` If the specified item and
  quantity do exist within `items`, decrement the item's stock by the
  specified quantity and return the updated dictionary.

  Write your solution for `pop_stock` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `pop_stock` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def pop_stock(items, item_name, quantity):
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

grade(pop_stock)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'chocolate': 20, 'candy': 5, 'chips': 10}, 'candy', 2, expected={'chocolate': 20, 'candy': 3, 'chips': 10})   # checks the value your code returns against this example
