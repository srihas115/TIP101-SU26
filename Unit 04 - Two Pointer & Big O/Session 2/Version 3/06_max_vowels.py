def max_vowels(s, k):
    pass

s = "abciiidef"
print(max_vowels(s, 3))

print(max_vowels(s, 5))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - no vowels at all")
print("  expected:", 0, "| got:", max_vowels("xyz", 2))

print("Test 2 - k equals the length of s (whole string is the window)")
print("  expected:", 3, "| got:", max_vowels("aeixyz", 6))

print("Test 3 - k is 1")
print("  expected:", 1, "| got:", max_vowels("xay", 1))


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

grade(max_vowels)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('abciiidef', 3, expected=3)   # checks the value your code returns against this example
