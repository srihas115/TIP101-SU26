'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 1  ·  Version 2
  Problem 7: Ternary Search

  Ternary search is a search algorithm that, similar to binary search, works
  on a sorted array. However, instead of dividing the search interval into
  two halves (as in binary search), ternary search divides it into three
  parts, using two midpoints. This reduces the problem size to approximately
  one-third in each step, rather than one-half.

  Given the pseudocode for `ternary_search()` below, implement the function.
  Evaluate the time and space complexity of your solution

  Write your solution for `ternary_search` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `ternary_search` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def ternary_search(lst, target):
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

grade(ternary_search)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 3, 5, 7, 9, 11, 13, 15], 11, expected=5)   # checks the value your code returns against this example
