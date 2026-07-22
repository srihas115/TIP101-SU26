'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 1  ·  Version 3
  Problem 5: Binary Search III

  Binary search is a searching algorithm that allows us to efficiently find
  the index of a given value within a sorted list. Given the pseudo code for
  binary search below, implement an iterative (non-recursive) implementation
  of binary search that returns `True` if the given target is in the list
  and `False` otherwise. There is also a recursive alternative that we’ll
  cover in the session 2 problem set!

  Evaluate the time and space complexity of your implementation.

  Write your solution for `binary_search` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `binary_search` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def binary_search(lst, target):
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

grade(binary_search)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 3, 5, 7, 9, 11, 13, 15], 11, expected=True)   # checks the value your code returns against this example
