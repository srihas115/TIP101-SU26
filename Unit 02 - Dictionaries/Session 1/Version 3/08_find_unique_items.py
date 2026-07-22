def find_unique_items(list_a, list_b):
    pass

list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]
print(find_unique_items(list_a, list_b))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", {"carrot": True, "date": False}, "| got:", find_unique_items(["apple","banana","carrot"], ["apple","banana","date"]))

print("Test 2 - identical lists (no unique items)")
print("  expected:", {}, "| got:", find_unique_items(["a","b"], ["a","b"]))

print("Test 3 - completely disjoint lists")
print("  expected:", {"x": True, "y": False}, "| got:", find_unique_items(["x"], ["y"]))

print("Test 4 - empty lists")
print("  expected:", {}, "| got:", find_unique_items([], []))

print("Test 5 - list_a empty, list_b has items")
print("  expected:", {"z": False}, "| got:", find_unique_items([], ["z"]))


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
