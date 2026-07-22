'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 2
  Problem 4: Find Odd Occurrences

  Write a function `find_odd_occurrences()` that takes in a list of integers
  `numbers` where all numbers occur an even number of times except for two
  unique numbers that occur an odd number of times. The function should find
  the two unique numbers and return them as a list. Assume each problem has
  exactly one solution.

  Write your solution for `find_odd_occurrences` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_odd_occurrences` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_odd_occurrences(numbers):
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

grade(find_odd_occurrences)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 4, 2, 3, 2, 3, 3, 4, 4, 4], expected=[1, 3])   # checks the value your code returns against this example
