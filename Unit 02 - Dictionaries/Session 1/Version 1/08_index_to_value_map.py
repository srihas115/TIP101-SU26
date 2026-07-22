def index_to_value_map(lst):
    res = {}
    for i in range(len(lst)):
        res[i] = lst[i]
    return res

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - example from spec")
print("  expected:", {0: "apple", 1: "banana", 2: "cherry"}, "| got:", index_to_value_map(["apple", "banana", "cherry"]))

print("Test 2 - empty list")
print("  expected:", {}, "| got:", index_to_value_map([]))

print("Test 3 - single element list")
print("  expected:", {0: "solo"}, "| got:", index_to_value_map(["solo"]))

print("Test 4 - duplicate values at different indices")
print("  expected:", {0: "a", 1: "a", 2: "b"}, "| got:", index_to_value_map(["a", "a", "b"]))

print("Test 5 - list of integers, including negatives and zero")
print("  expected:", {0: -1, 1: 0, 2: 5}, "| got:", index_to_value_map([-1, 0, 5]))


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

grade(index_to_value_map)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['apple', 'banana', 'cherry'], expected={0: 'apple', 1: 'banana', 2: 'cherry'})   # checks the value your code returns against this example
