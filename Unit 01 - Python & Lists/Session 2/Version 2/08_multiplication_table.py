def multiplication_table(num):
    pass

multiplication_table(7)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - num is 1 (prints 1 through 10)")
print("  expected printed output: 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10")
multiplication_table(1)

print("Test 2 - num is 0 (prints ten zeroes)")
print("  expected printed output: 0 (ten times)")
multiplication_table(0)

print("Test 3 - negative num")
print("  expected printed output: -2 / -4 / -6 / -8 / -10 / -12 / -14 / -16 / -18 / -20")
multiplication_table(-2)


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

grade(multiplication_table)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(7, expected='7\n14\n21\n28\n35\n42\n49\n56\n63\n70')   # checks the printed output against this example
