def count_negatives(k, nums):
    pass

lst = [-1, 2, -2, 3, 5, -7, -5]
print(count_negatives(lst, 3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.
# Note: calls follow the same (list, k) argument order as the example call above.

print("Test 1 - k equals the length of the list (single window)")
print("  expected:", [2], "| got:", count_negatives([-1,-2,3], 3))

print("Test 2 - no negatives at all")
print("  expected:", [0,0,0], "| got:", count_negatives([1,2,3,4], 2))

print("Test 3 - all negative")
print("  expected:", [2,2], "| got:", count_negatives([-1,-2,-3], 2))


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

grade(count_negatives)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(3, [-1, 2, -2, 3, 5, -7, -5], expected=[2, 1, 1, 1, 2])   # checks the value your code returns against this example
