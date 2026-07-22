def counter(stop):
    for i in range(stop):
        print(i+1)

counter(7)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - stop is 1 (prints just 1)")
print("  expected printed output: 1")
counter(1)

print("Test 2 - stop is 0 (no numbers printed)")
print("  expected printed output: (nothing)")
counter(0)

print("Test 3 - negative stop (no numbers printed)")
print("  expected printed output: (nothing)")
counter(-5)

print("Test 4 - stop is 3")
print("  expected printed output: 1 / 2 / 3")
counter(3)


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

grade(counter)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(7, expected='1\n2\n3\n4\n5\n6\n7')   # checks the printed output against this example
