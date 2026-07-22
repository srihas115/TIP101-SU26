'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 2  ·  Version 1
  Problem 6: Sum Unique Elements

  Write a function `sum_of_unique_elements()` that takes in two lists of
  integers, `lst1` and `lst2`, as parameters and returns the sum of the
  elements that are *unique* in `lst1`.

  An element is *unique* if: - it appears exactly once in `lst1` - it does
  not appear in `lst2`

  Write your solution for `sum_of_unique_elements` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `sum_of_unique_elements` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def sum_of_unique_elements(lst1, lst2):
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

grade(sum_of_unique_elements)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4], [3, 4, 5, 6], expected=3)   # checks the value your code returns against this example
