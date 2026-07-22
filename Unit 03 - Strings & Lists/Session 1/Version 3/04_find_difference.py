def find_difference(s1, s2):
    pass

s1 = "abcd"
s2 = "baedc"
print(find_difference(s1, s2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - minimal case, single character strings")
print("  expected:", "b", "| got:", find_difference("a", "ba"))

print("Test 2 - added letter is a duplicate of an existing letter")
print("  expected:", "a", "| got:", find_difference("aa", "aaa"))

print("Test 3 - longer strings")
print("  expected:", "z", "| got:", find_difference("abcdef", "fecdzba"))


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

grade(find_difference)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('abcd', 'baedc', expected='e')   # checks the value your code returns against this example
