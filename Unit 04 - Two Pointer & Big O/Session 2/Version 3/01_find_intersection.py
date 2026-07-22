'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 3
  Problem 1: List Intersection

  Using the two_pointer approach, write a function `find_intersection()`
  that takes in two *sorted* lists as parameters and returns a list
  containing the intersection of the two lists. The intersection list should
  also be sorted.

  The **two-pointer approach** is a common technique in which we initialize
  two variables (also called a pointer in this context) to track different
  indices or places in a list or string, then moves the pointers to point at
  new indices based on certain conditions. A common variation of this
  technique is to point one variable at the beginning of one list/string and
  a second pointer at the beginning of a second list/string, then increment
  each pointer conditionally to solve a problem.

  Write your solution for `find_intersection` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_intersection` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_intersection(lst1, lst2):
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

grade(find_intersection)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 4, 6, 7], [2, 3, 4, 7], expected=[2, 4, 7])   # checks the value your code returns against this example
