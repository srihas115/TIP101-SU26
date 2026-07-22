'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 2
  Problem 2: Checking Subsequence

  Write a function `is_subsequence` that takes in two strings `s` and `t` as
  parameters and returns `True` if `s` is a subsequence of `t` and `False`
  otherwise.

  A **subsequence** of a string is a new string that is formed from the
  original string by deleting some or none of the characters without
  disturbing the relative positions of the remaining characters. (*i.e.,
  "ace" is a subsequence of "abcde" while "aec" is not*).

  Write your solution for `is_subsequence` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `is_subsequence` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def is_subsequence(s, t):
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

grade(is_subsequence)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('abc', 'ahbgdc', expected=True)   # checks the value your code returns against this example
