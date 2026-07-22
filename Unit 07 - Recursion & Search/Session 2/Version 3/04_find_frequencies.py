'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 2  ·  Version 3
  Problem 4: Find Frequencies

  Given a sorted list of integers containing duplicates, write a function
  `find_frequencies()` that finds each element’s frequency in less than
  `O(n)` time.

  Write your solution for `find_frequencies` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_frequencies` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_frequencies(lst):
    pass

# Example Input: [2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9]


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

grade(find_frequencies)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9], expected={2: 3, 4: 3, 5: 2, 6: 1, 8: 2, 9: 1})   # checks the value your code returns against this example
