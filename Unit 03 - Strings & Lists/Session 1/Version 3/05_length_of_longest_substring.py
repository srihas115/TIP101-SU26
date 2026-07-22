def length_of_longest_substring(s):
    pass

s = "abcdeefghhhhh"
count = length_of_longest_substring(s)
print(count)

s2 = "aaaaaaaaaaaaaaa"
count = length_of_longest_substring(s2)
print(count)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", 0, "| got:", length_of_longest_substring(""))

print("Test 2 - single character")
print("  expected:", 1, "| got:", length_of_longest_substring("a"))

print("Test 3 - all unique characters")
print("  expected:", 4, "| got:", length_of_longest_substring("abcd"))

print("Test 4 - two identical characters")
print("  expected:", 1, "| got:", length_of_longest_substring("aa"))


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

grade(length_of_longest_substring)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('abcdeefghhhhh', expected=5)   # checks the value your code returns against this example
