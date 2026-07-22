def first_unique_char(my_str):
    pass

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string has no unique char")
print("  expected:", -1, "| got:", first_unique_char(""))

print("Test 2 - single character string")
print("  expected:", 0, "| got:", first_unique_char("z"))

print("Test 3 - all-same-character string has no unique char")
print("  expected:", -1, "| got:", first_unique_char("aaaa"))

print("Test 4 - mixed case treats 'A' and 'a' as different characters")
print("  expected:", 0, "| got:", first_unique_char("Aa"))

print("Test 5 - unique char is the last character")
print("  expected:", 3, "| got:", first_unique_char("aabbc"))

print("Test 6 - string with whitespace and punctuation")
print("  expected:", 0, "| got:", first_unique_char("a a"))


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

grade(first_unique_char)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('leetcode', expected=0)   # checks the value your code returns against this example
