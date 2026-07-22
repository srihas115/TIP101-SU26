def get_last(lst):
    if len(lst) == 0:
        return None
    return lst[len(lst) - 1]

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", None, "| got:", get_last([]))

print("Test 2 - single-element list")
print("  expected:", 9, "| got:", get_last([9]))

print("Test 3 - unsorted list")
print("  expected:", 2, "| got:", get_last([4,1,3,2]))

print("Test 4 - list with negative numbers")
print("  expected:", -3, "| got:", get_last([-7,-1,-3]))

print("Test 5 - already-sorted list")
print("  expected:", 4, "| got:", get_last([1,2,3,4]))


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

grade(get_last)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, 1, 6, 7, 5], expected=5)   # checks the value your code returns against this example
