def count_good_substrings(s):
    pass

s1 = "xyzzaz"
s2 = "xyzxyz"
print(count_good_substrings(s1))
print(count_good_substrings(s2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - string shorter than 3 characters")
print("  expected:", 0, "| got:", count_good_substrings("xy"))

print("Test 2 - exactly length 3, no repeats")
print("  expected:", 1, "| got:", count_good_substrings("xyz"))

print("Test 3 - exactly length 3, has a repeat")
print("  expected:", 0, "| got:", count_good_substrings("xyx"))

print("Test 4 - empty string")
print("  expected:", 0, "| got:", count_good_substrings(""))


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

grade(count_good_substrings)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('xyzzaz', expected=1)   # checks the value your code returns against this example
