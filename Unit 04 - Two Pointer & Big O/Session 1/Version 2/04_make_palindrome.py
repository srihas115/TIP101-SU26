'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 2
  Problem 4: Make Palindromes

  You are given a string `s` consisting of lowercase English letters, and
  are allowed to perform operations on it. In one operation, you can
  **replace a character** in `s` with another lowercase English letter.

  Write a function `make_palindrome()` that takes in a string `s` and turns
  it into a palindrome with the minimum number of operations as possible. If
  there are multiple palindromes that can be made using the minimum number
  of operations, make the **lexicographically smallest** one.

  A string `a` is lexicographically smaller than a string `b` (*of the same
  length*) if in the first position where `a` and `b` differ, string `a` has
  a letter that appears earlier in the alphabet than the corresponding
  letter in `b`.

  The function returns the resulting palindrome string.

  Write your solution for `make_palindrome` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `make_palindrome` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def make_palindrome(s):
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

grade(make_palindrome)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('egcfe', expected='efcfe')   # checks the value your code returns against this example
