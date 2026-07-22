def print_odd_indices(nums):
    pass

nums = [3,4,8,1,5,2]
print_odd_indices(nums)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (nothing printed)")
print("  expected printed output: (nothing)")
print_odd_indices([])

print("Test 2 - single-element list (no odd indices, nothing printed)")
print("  expected printed output: (nothing)")
print_odd_indices([9])

print("Test 3 - two-element list (only index 1 printed)")
print("  expected printed output: 20")
print_odd_indices([10, 20])

print("Test 4 - list with duplicate values")
print("  expected printed output: 5 / 5")
print_odd_indices([5,5,5,5])


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

grade(print_odd_indices)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, 4, 8, 1, 5, 2], expected='4\n1\n2')   # checks the printed output against this example
