def contains_nearby_duplicate(lst, k):
    pass

lst = [1, 2, 3, 1, 2, 3]
lst2 = [1, 0, 1, 1]
print(contains_nearby_duplicate(lst, 2))
print(contains_nearby_duplicate(lst2, 1))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - k greater than list length, duplicate exists somewhere")
print("  expected:", True, "| got:", contains_nearby_duplicate([1,2,3,1], 100))

print("Test 2 - no duplicates at all")
print("  expected:", False, "| got:", contains_nearby_duplicate([1,2,3,4], 3))

print("Test 3 - duplicate exactly at k distance (boundary)")
print("  expected:", True, "| got:", contains_nearby_duplicate([1,2,3,1], 3))

print("Test 4 - empty list")
print("  expected:", False, "| got:", contains_nearby_duplicate([], 2))


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

grade(contains_nearby_duplicate)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 1, 2, 3], 2, expected=False)   # checks the value your code returns against this example
