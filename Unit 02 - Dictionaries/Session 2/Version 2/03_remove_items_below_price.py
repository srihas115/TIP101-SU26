'''
==============================================================================
    Unit 2: Dictionaries  ·  Session 2  ·  Version 2
    Problem 3: Filter by Price

    Write a function that takes in a dictionary of `items` and a
    `price_threshold` as parameters. The function should iterate through the
    dictionary and remove all items that has a value less than
    `price_threshold`. The function also returns a list of all items that are
    removed. If no item satisfies the condition, return `None`.

    Write your solution for `remove_items_below_price` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `remove_items_below_price` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def remove_items_below_price(items, price_threshold):
    pass

items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
print(removed_list)
removed_list_two = remove_items_below_price(items, 1.00)
print(removed_list_two)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty dict")
print("  expected:", None, "| got:", remove_items_below_price({}, 1.00))

print("Test 2 - threshold so low nothing is removed")
print("  expected:", None, "| got:", remove_items_below_price({"apple": 1.99}, 0.01))

print("Test 3 - threshold removes every item")
print("  expected:", ["apple", "banana"], "| got:", remove_items_below_price({"apple": 1.00, "banana": 2.00}, 5.00))

print("Test 4 - single item removed")
print("  expected:", ["cheap"], "| got:", remove_items_below_price({"cheap": 0.50, "pricey": 9.99}, 1.00))


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

grade(remove_items_below_price)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'apple': 1.99, 'banana': 0.99, 'cherry': 3.49, 'date': 0.69}, 1.0, expected=['banana', 'date'])   # checks the value your code returns against this example
