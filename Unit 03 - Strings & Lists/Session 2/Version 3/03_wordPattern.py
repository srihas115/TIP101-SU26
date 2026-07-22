def wordPattern(pattern, s):
    pass

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
s2 = "dog cat cat fish"
print(wordPattern(pattern, s2))

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(wordPattern(pattern2, s3))
s4 = "dog dog dog dog"
print(wordPattern(pattern2, s4))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - pattern length does not match word count")
print("  expected:", False, "| got:", wordPattern("ab", "dog dog dog"))

print("Test 2 - single-character pattern, single word")
print("  expected:", True, "| got:", wordPattern("a", "dog"))

print("Test 3 - different pattern letters mapped to the same word (violates 1:1)")
print("  expected:", False, "| got:", wordPattern("ab", "dog dog"))


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

grade(wordPattern)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('abba', 'dog cat cat dog', expected=True)   # checks the value your code returns against this example
