def first_repeated_char(s):
    pass

s = "hello world"
s2 = "aAbBCC"
s3 = "abcdefg"

print(first_repeated_char(s))
print(first_repeated_char(s2))
print(first_repeated_char(s3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", None, "| got:", first_repeated_char(""))

print("Test 2 - single character")
print("  expected:", None, "| got:", first_repeated_char("a"))

print("Test 3 - duplicate at the very start")
print("  expected:", 1, "| got:", first_repeated_char("aab"))

print("Test 4 - all-same-character string")
print("  expected:", 1, "| got:", first_repeated_char("aaa"))


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

grade(first_repeated_char)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('hello world', expected=3)   # checks the value your code returns against this example
