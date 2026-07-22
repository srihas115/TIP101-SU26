def is_palindrome(s):
    pass

s = "amanaplanacanalpanama"
s2 = "helloworld"

print(is_palindrome(s))
print(is_palindrome(s2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string (vacuously a palindrome)")
print("  expected:", True, "| got:", is_palindrome(""))

print("Test 2 - single character")
print("  expected:", True, "| got:", is_palindrome("a"))

print("Test 3 - two identical characters")
print("  expected:", True, "| got:", is_palindrome("aa"))

print("Test 4 - two different characters")
print("  expected:", False, "| got:", is_palindrome("ab"))

print("Test 5 - all-same-character string")
print("  expected:", True, "| got:", is_palindrome("aaaa"))


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

grade(is_palindrome)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('amanaplanacanalpanama', expected=True)   # checks the value your code returns against this example
