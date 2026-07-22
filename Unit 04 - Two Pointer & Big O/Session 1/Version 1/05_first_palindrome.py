'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 1
  Problem 5: Palindrome

  Write a function `first_palindrome()` that takes in a list of strings
  `words` as a parameter and returns the first palindromic string in the
  list. A string is **palindromic** if it reads the same forward and
  backward. If there is no such string, return an empty string `""`

  Write your solution for `first_palindrome` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `first_palindrome` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def first_palindrome(words):
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

grade(first_palindrome)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['abc', 'car', 'ada', 'racecar', 'cool'], expected='ada')   # checks the value your code returns against this example
