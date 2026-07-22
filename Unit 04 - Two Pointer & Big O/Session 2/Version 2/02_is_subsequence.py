def is_subsequence(s, t):
    pass

s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))

a = "cba"
b = "ahbgdc"
print(is_subsequence(a, b))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty s (empty string is a subsequence of anything)")
print("  expected:", True, "| got:", is_subsequence("", "abc"))

print("Test 2 - s equals t")
print("  expected:", True, "| got:", is_subsequence("abc", "abc"))

print("Test 3 - s longer than t")
print("  expected:", False, "| got:", is_subsequence("abcd", "abc"))

print("Test 4 - empty t, non-empty s")
print("  expected:", False, "| got:", is_subsequence("a", ""))


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

grade(is_subsequence)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('abc', 'ahbgdc', expected=True)   # checks the value your code returns against this example
