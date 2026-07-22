def binary_substrings_count(s):
    pass

s = "00110011"
print(binary_substrings_count(s))

s2 = "10101"
print(binary_substrings_count(s2))

s3 = "1111"
print(binary_substrings_count(s3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", 0, "| got:", binary_substrings_count(""))

print("Test 2 - single character")
print("  expected:", 0, "| got:", binary_substrings_count("0"))

print("Test 3 - minimal valid substring '01'")
print("  expected:", 1, "| got:", binary_substrings_count("01"))

print("Test 4 - minimal valid substring '10'")
print("  expected:", 1, "| got:", binary_substrings_count("10"))


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

grade(binary_substrings_count)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('00110011', expected=6)   # checks the value your code returns against this example
