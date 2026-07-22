'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 2  ·  Version 2
  Problem 1: Update Score

  Write a function `update_score()` that takes in a dictionary `scores` that
  maps player names to current scores, a string `player`, and an integer
  `points` as parameters. The function adds the `points` to the current
  score of `player` in the dictionary and returns the updated dictionary. If
  the player does not exist in `scores`, then add them.

  Write your solution for `update_score` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `update_score` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def update_score(scores, player, points):
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

grade(update_score)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'Alice': 100, 'Bob': 90}, 'Alice', 10, expected={'Alice': 110, 'Bob': 90})   # checks the value your code returns against this example
