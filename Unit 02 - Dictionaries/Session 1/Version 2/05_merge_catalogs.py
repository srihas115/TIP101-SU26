def merge_catalogs(catalog1, catalog2):
    pass

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
print(merge_catalogs(catalog1, catalog2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - both catalogs empty")
print("  expected:", {}, "| got:", merge_catalogs({}, {}))

print("Test 2 - first catalog empty, second has items")
print("  expected:", {"apple": 2.0}, "| got:", merge_catalogs({}, {"apple": 2.0}))

print("Test 3 - second catalog empty, first has items")
print("  expected:", {"apple": 2.0}, "| got:", merge_catalogs({"apple": 2.0}, {}))

print("Test 4 - no overlapping products, both keep their prices")
print("  expected:", {"apple": 1.0, "banana": 2.0}, "| got:", merge_catalogs({"apple": 1.0}, {"banana": 2.0}))

print("Test 5 - overlapping product with identical price in both catalogs")
print("  expected:", {"apple": 1.0}, "| got:", merge_catalogs({"apple": 1.0}, {"apple": 1.0}))


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
