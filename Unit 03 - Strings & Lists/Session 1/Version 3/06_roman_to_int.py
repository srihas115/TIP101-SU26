def roman_to_int(s):
    pass

s = "XL"
print(roman_to_int(s))

s2 = "LVIII"
print(roman_to_int(s2))

s3 = "MCMXCIV"
print(roman_to_int(s3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single character")
print("  expected:", 1, "| got:", roman_to_int("I"))

print("Test 2 - subtractive pair (IV)")
print("  expected:", 4, "| got:", roman_to_int("IV"))

print("Test 3 - subtractive pair (IX)")
print("  expected:", 9, "| got:", roman_to_int("IX"))

print("Test 4 - repeated same symbol, no subtraction")
print("  expected:", 3, "| got:", roman_to_int("III"))

print("Test 5 - larger mixed numeral")
print("  expected:", 2024, "| got:", roman_to_int("MMXXIV"))


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

grade(roman_to_int)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('XL', expected=40)   # checks the value your code returns against this example
