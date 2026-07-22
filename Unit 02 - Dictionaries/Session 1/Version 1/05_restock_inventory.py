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
    for k, v in restock_list.items():
        current_inventory[k] = current_inventory.get(k, 0) + v
    return current_inventory

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
print(restock_inventory(current_inventory, restock_list))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty restock list (inventory unchanged)")
print("  expected:", {"apples": 30, "bananas": 15}, "| got:", restock_inventory({"apples": 30, "bananas": 15}, {}))

print("Test 2 - empty current inventory (all items new)")
print("  expected:", {"apples": 10, "pears": 5}, "| got:", restock_inventory({}, {"apples": 10, "pears": 5}))

print("Test 3 - restock item not in current inventory")
print("  expected:", {"apples": 30, "kiwis": 8}, "| got:", restock_inventory({"apples": 30}, {"kiwis": 8}))

print("Test 4 - restock quantity of 0 (item stays the same)")
print("  expected:", {"apples": 30}, "| got:", restock_inventory({"apples": 30}, {"apples": 0}))

print("Test 5 - both dictionaries empty")
print("  expected:", {}, "| got:", restock_inventory({}, {}))

print("Test 6 - multiple new items added at once")
print("  expected:", {"apples": 30, "kiwis": 4, "mangoes": 2}, "| got:", restock_inventory({"apples": 30}, {"kiwis": 4, "mangoes": 2}))


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
