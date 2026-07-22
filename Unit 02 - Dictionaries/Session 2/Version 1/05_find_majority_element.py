'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 1
  Problem 5: Find Majority Element

  Write a function `find_majority_element()` that takes in a list of
  integers `elements` and finds the majority element in the list. A majority
  element is an element that appears more than `n/2` times where `n` is the
  size of the list. If there is no majority element, return `None`.

  Write your solution for `find_majority_element` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_majority_element` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_majority_element(elements):
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

grade(find_majority_element)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([2, 2, 1, 1, 1, 2, 2], expected=2)   # checks the value your code returns against this example
