def find_highest_exponent(base, limit):
    pass

exp = find_highest_exponent(2, 100)
print(exp)

exp2 = find_highest_exponent(3, 5)
print(exp2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - limit less than base (exponent 0 still fits)")
print("  expected:", 0, "| got:", find_highest_exponent(5, 1))

print("Test 2 - limit is an exact power of base")
print("  expected:", 6, "| got:", find_highest_exponent(2, 64))

print("Test 3 - larger base and limit")
print("  expected:", 3, "| got:", find_highest_exponent(10, 1000))


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

grade(find_highest_exponent)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(2, 100, expected=6)   # checks the value your code returns against this example
