'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 2
  Problem 2: 2-Pointer Palindrome

  Write a function `is_palindrome()` that takes in a string `s` as a
  parameter and returns `True` if the string is a palindrome and `False`
  otherwise. You may assume the string contains only lowercase alphabetic
  characters.

  The function must use the **two-pointer approach**, which is a common
  technique in which we initialize two variables (also called a pointer in
  this context) to track different indices or places in a list or string,
  then moves the pointers to point at new indices based on certain
  conditions. In the most common variation of the two-pointer approach, we
  initialize one variable to point at the beginning of a list and a second
  variable/pointer to point at the end of list. We then shift the pointers
  to move inwards through the list towards each other, until our problem is
  solved or the pointers reach the opposite ends of the list.

  Write your solution for `is_palindrome` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `is_palindrome` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def is_palindrome(s):
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

grade(is_palindrome)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('amanaplanacanalpanama', expected=True)   # checks the value your code returns against this example
