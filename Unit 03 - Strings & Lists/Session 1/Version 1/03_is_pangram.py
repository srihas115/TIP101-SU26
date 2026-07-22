'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 1  ·  Version 1
  Problem 3: Is Pangram

  Write a function `is_pangram()` that takes in a string `my_str` as a
  parameter and returns `True` if the string is a **pangram** and `False` if
  not. A **pangram** is a sentence containing every letter in the English
  alphabet.

  Write your solution for `is_pangram` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `is_pangram` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def is_pangram(my_str):
    pass

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string is not a pangram")
print("  expected:", False, "| got:", is_pangram(""))

print("Test 2 - single character string is not a pangram")
print("  expected:", False, "| got:", is_pangram("a"))

print("Test 3 - all 26 letters lowercase exactly once")
print("  expected:", True, "| got:", is_pangram("abcdefghijklmnopqrstuvwxyz"))

print("Test 4 - all 26 letters with mixed case")
print("  expected:", True, "| got:", is_pangram("ABCdefGHIjklMNOpqrSTUvwxYZ"))

print("Test 5 - pangram with punctuation and repeated letters")
print("  expected:", True, "| got:", is_pangram("Pack my box with five dozen liquor jugs!"))

print("Test 6 - missing one letter (z) should not be a pangram")
print("  expected:", False, "| got:", is_pangram("abcdefghijklmnopqrstuvwxy"))


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

grade(is_pangram)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('The quick brown fox jumps over the lazy dog', expected=True)   # checks the value your code returns against this example
