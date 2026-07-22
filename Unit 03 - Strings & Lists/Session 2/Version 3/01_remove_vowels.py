'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 2  ·  Version 3
  Problem 1: Remove Vowels

  Write a function `remove_vowels()` that takes in a string `s` as a
  parameter and returns a new string with all the vowels removed. For the
  purposes of this exercise, consider **a**, **e**, **i**, **o**, and **u**
  as vowels and not **y**. The function should preserve the case of the
  original letters.

  Write your solution for `remove_vowels` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `remove_vowels` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def remove_vowels(s):
    pass

s = "Hello World"
new_string = remove_vowels(s)
print(new_string)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", "", "| got:", remove_vowels(""))

print("Test 2 - all vowels")
print("  expected:", "", "| got:", remove_vowels("aeiou"))

print("Test 3 - no vowels (unchanged)")
print("  expected:", "xyz", "| got:", remove_vowels("xyz"))

print("Test 4 - mixed case vowels, consonant case preserved")
print("  expected:", "xYz", "| got:", remove_vowels("xAeYIoUz"))

print("Test 5 - single vowel character")
print("  expected:", "", "| got:", remove_vowels("a"))

print("Test 6 - single consonant character")
print("  expected:", "b", "| got:", remove_vowels("b"))


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

grade(remove_vowels)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('Hello World', expected='Hll Wrld')   # checks the value your code returns against this example
