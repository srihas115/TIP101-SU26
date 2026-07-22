'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 2
  Problem 5: Reverse Vowels

  Write a function `reverse_vowels()` that takes in a string `s` as a
  parameter and returns a string with all the vowels in the string reversed.
  The consonants should remain in the same position. For this question, we
  consider **a**, **e**, **i**, **o**, and **u** as vowels but not **y**.
  The vowels can appear in both lower and upper cases, more than once.

  Write your solution for `reverse_vowels` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `reverse_vowels` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def reverse_vowels(s):
    pass  # replace this line with your solution













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

grade(reverse_vowels)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('hello', expected='holle')   # checks the value your code returns against this example
