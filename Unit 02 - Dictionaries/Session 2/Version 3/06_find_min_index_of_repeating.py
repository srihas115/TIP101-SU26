'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 3
  Problem 6: First Repeating Element

  Write a function `find_min_index_of_repeating()` that takes in an integer
  list `nums` as a parameter and returns the minimum index of an element
  that has a duplicate value. The function should only do a single traversal
  of the list. If there are no repeating elements, return `None`.

  Write your solution for `find_min_index_of_repeating` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_min_index_of_repeating` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_min_index_of_repeating(nums):
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

grade(find_min_index_of_repeating)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 6, 3, 4, 3, 6, 4], expected=1)   # checks the value your code returns against this example
