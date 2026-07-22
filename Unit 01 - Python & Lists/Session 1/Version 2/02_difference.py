def difference(a, b):
    return a-b

diff = difference(8, 3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - a=8, b=3 (matches example)")
print("  expected:", 5, "| got:", difference(8, 3))

print("Test 2 - b greater than a (negative result)")
print("  expected:", -5, "| got:", difference(3, 8))

print("Test 3 - a equals b (zero result)")
print("  expected:", 0, "| got:", difference(4, 4))

print("Test 4 - both zero")
print("  expected:", 0, "| got:", difference(0, 0))

print("Test 5 - negative numbers")
print("  expected:", -3, "| got:", difference(-5, -2))


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

grade(difference)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(8, 3, expected=5)   # checks the value your code returns against this example
