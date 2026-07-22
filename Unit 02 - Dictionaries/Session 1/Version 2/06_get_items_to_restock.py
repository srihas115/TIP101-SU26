'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 2
  Problem 6: Items to Restock

  Write a function `get_items_to_restock()` that takes in a dictionary
  `products` that maps product names to their quantities and an integer
  `restock_threshold` as parameters. The function returns a list of products
  that have a value less than `restock_threshold` and need to be restocked.
  If `products` is empty, the function return an empty list.

  Write your solution for `get_items_to_restock` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `get_items_to_restock` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def get_items_to_restock(products, restock_threshold):
    pass

products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5
print(get_items_to_restock(products, restock_threshold))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty products dictionary")
print("  expected:", [], "| got:", get_items_to_restock({}, 5))

print("Test 2 - all quantities below threshold")
print("  expected:", ["Product1", "Product2"], "| got:", get_items_to_restock({"Product1": 1, "Product2": 2}, 5))

print("Test 3 - all quantities equal to threshold (not restocked, since it must be strictly less)")
print("  expected:", [], "| got:", get_items_to_restock({"Product1": 5, "Product2": 5}, 5))

print("Test 4 - all quantities above threshold")
print("  expected:", [], "| got:", get_items_to_restock({"Product1": 10, "Product2": 20}, 5))

print("Test 5 - threshold of 0 (nothing needs restocking)")
print("  expected:", [], "| got:", get_items_to_restock({"Product1": 3, "Product2": 0}, 0))

print("Test 6 - single product below threshold")
print("  expected:", ["Product1"], "| got:", get_items_to_restock({"Product1": 1}, 5))


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

grade(get_items_to_restock)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'Product1': 10, 'Product2': 2, 'Product3': 5, 'Product4': 3}, 5, expected=['Product2', 'Product4'])   # checks the value your code returns against this example
