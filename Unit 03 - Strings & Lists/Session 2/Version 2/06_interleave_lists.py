'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 2  ·  Version 2
  Problem 6: Interleave Lists

  Write a function `interleave_lists()` that accepts two lists as
  parameters. The function should return a new list that combines the given
  lists by alternating which list it takes its next element from. It will
  take elements in order, and if one list is longer it will append the
  remaining elements to the end of the interleaved list.

  Write your solution for `interleave_lists` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `interleave_lists` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def interleave_lists(lst1, lst2):
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

grade(interleave_lists)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4], [10, 20], expected=[1, 10, 2, 20, 3, 4])   # checks the value your code returns against this example
