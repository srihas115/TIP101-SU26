'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 2  ·  Version 3
  Problem 4: Binary Substrings

  Write a function `binary_substrings_count()` that takes in a string `s`
  representing a binary number as a parameter. The function counts the
  number of substrings that satisfy all of the following conditions: -
  contains an equal number of `0`s and `1`s - all the `0`s in the substring
  are grouped consecutively - all the `1`s in the substrings are grouped
  consecutively

  Write your solution for `binary_substrings_count` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `binary_substrings_count` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def binary_substrings_count(s):
    pass

s = "00110011"
print(binary_substrings_count(s))

s2 = "10101"
print(binary_substrings_count(s2))

s3 = "1111"
print(binary_substrings_count(s3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", 0, "| got:", binary_substrings_count(""))

print("Test 2 - single character")
print("  expected:", 0, "| got:", binary_substrings_count("0"))

print("Test 3 - minimal valid substring '01'")
print("  expected:", 1, "| got:", binary_substrings_count("01"))

print("Test 4 - minimal valid substring '10'")
print("  expected:", 1, "| got:", binary_substrings_count("10"))


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

grade(binary_substrings_count)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('00110011', expected=6)   # checks the value your code returns against this example
