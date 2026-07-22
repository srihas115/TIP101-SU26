'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 2  ·  Version 2
  Problem 2: How Many 0s (Iterative)

  Given a sorted list of integers containing only 0s and 1s, count the total
  number of 0’s in the array in `O(log n)` time.

  Write your solution for `count_zeroes` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `count_zeroes` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def count_zeroes(lst):
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

grade(count_zeroes)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([0, 0, 0, 0, 1, 1, 1], expected=4)   # checks the value your code returns against this example
