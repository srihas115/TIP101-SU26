def doubled(lst):
    for item in lst:
        print(int(item * 2))
        
lst = [1,2,3]
print(doubled(lst))

print()

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (nothing printed)")
print("  expected printed output: (nothing)")
doubled([])

print("Test 2 - negative numbers")
print("  expected printed output: -2 / -4")
doubled([-1, -2])

print("Test 3 - single-element list")
print("  expected printed output: 10")
doubled([5])

print("Test 4 - list containing zero")
print("  expected printed output: 0 / 6")
doubled([0, 3])


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

grade(doubled)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], expected='2\n4\n6')   # checks the printed output against this example
