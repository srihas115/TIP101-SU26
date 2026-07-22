def print_indices(lst):
    for i in range(len(lst)):
        print(i)

lst = [5,1,3,8,2]
print_indices(lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (nothing printed)")
print("  expected printed output: (nothing)")
print_indices([])

print("Test 2 - single-element list")
print("  expected printed output: 0")
print_indices(["a"])

print("Test 3 - three-element list")
print("  expected printed output: 0 / 1 / 2")
print_indices(["a", "b", "c"])


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

grade(print_indices)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 1, 3, 8, 2], expected='0\n1\n2\n3\n4')   # checks the printed output against this example
