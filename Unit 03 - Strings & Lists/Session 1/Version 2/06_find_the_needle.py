def find_the_needle(haystack, needle):
    pass

haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty needle (found at the start)")
print("  expected:", 0, "| got:", find_the_needle("hello", ""))

print("Test 2 - needle equals haystack")
print("  expected:", 0, "| got:", find_the_needle("abc", "abc"))

print("Test 3 - needle not found")
print("  expected:", -1, "| got:", find_the_needle("abc", "xyz"))

print("Test 4 - single-character haystack and needle, matching")
print("  expected:", 0, "| got:", find_the_needle("a", "a"))


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

grade(find_the_needle)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('tobeornottobe', 'be', expected=2)   # checks the value your code returns against this example
