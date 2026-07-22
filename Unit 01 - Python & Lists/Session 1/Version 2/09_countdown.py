def countdown(m,n):
    for num in range(m, n-1, -1):
        print(num)

countdown(5,1)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - m equals n (prints just m)")
print("  expected printed output: 3")
countdown(3, 3)

print("Test 2 - m=1, n=1")
print("  expected printed output: 1")
countdown(1, 1)

print("Test 3 - m less than n (nothing to count down, no output)")
print("  expected printed output: (nothing)")
countdown(2, 5)

print("Test 4 - m=3, n=1")
print("  expected printed output: 3 / 2 / 1")
countdown(3, 1)


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

grade(countdown)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(5, 1, expected='5\n4\n3\n2\n1')   # checks the printed output against this example
