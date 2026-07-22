'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 1  ·  Version 2
  Problem 6: Needle in a Haystack

  Write a function `find_the_needle()` that takes in two string parameters:
  a `needle` and a `haystack`. The function returns the index of the first
  occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of
  `haystack`.

  Write your solution for `find_the_needle` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_the_needle` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_the_needle(haystack, needle):
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

grade(find_the_needle)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('tobeornottobe', 'be', expected=2)   # checks the value your code returns against this example
