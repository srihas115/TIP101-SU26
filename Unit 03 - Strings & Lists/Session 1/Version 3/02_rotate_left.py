'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 1  ·  Version 3
  Problem 2: Rotate Left

  Write a function `rotate_left()` that takes in a string `s` and an integer
  `n` as parameters. The function returns a new string with the first `n`
  characters moved to the end of the string where `1 <= n <= len(str)`.

  Write your solution for `rotate_left` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `rotate_left` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def rotate_left(s, n):
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

grade(rotate_left)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('rotation', 2, expected='tationro')   # checks the value your code returns against this example
