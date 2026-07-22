def count_consecutive_characters(str1):
    pass

str1 = "aaabbcaaaa"
count = count_consecutive_characters(str1)
print(count)
str2 = "abcde"
count2 = count_consecutive_characters(str2)
print(count2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", 0, "| got:", count_consecutive_characters(""))

print("Test 2 - single character")
print("  expected:", 1, "| got:", count_consecutive_characters("a"))

print("Test 3 - all-same-character string")
print("  expected:", 5, "| got:", count_consecutive_characters("aaaaa"))

print("Test 4 - multiple runs of the same max length")
print("  expected:", 2, "| got:", count_consecutive_characters("aabb"))


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

grade(count_consecutive_characters)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('aaabbcaaaa', expected=4)   # checks the value your code returns against this example
