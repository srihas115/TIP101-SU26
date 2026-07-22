'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 2  ·  Version 2
  Problem 6: Circle Majority

  Given an array `nums` of size `n`, use a divide and conquer approach to
  write a function return *the majority element*.

  The majority element is the element that appears more than `⌊n / 2⌋`
  times. You may assume that the majority element always exists in the
  array.

  Write your solution for `majority_element` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `majority_element` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def majority_element(nums):
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

grade(majority_element)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, 2, 3], expected=3)   # checks the value your code returns against this example
