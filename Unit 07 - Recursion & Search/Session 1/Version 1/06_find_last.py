'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 1  ·  Version 1
  Problem 6: Backwards Binary Search

  Generally binary search returns the index of the **first occurrence** of
  the `target` in the list. Write an updated version of binary search
  `find_last()` that, given a list that may contain duplicates, returns the
  index of the last occurrence of `target`.

  Evaluate the time and space complexity of your function.

  Write your solution for `find_last` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_last` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_last(lst, target):
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

grade(find_last)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 3, 5, 7, 9, 11, 11, 13, 15], 11, expected=6)   # checks the value your code returns against this example
