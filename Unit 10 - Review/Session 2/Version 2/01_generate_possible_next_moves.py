'''
==============================================================================
  Unit 10: Review  ·  Session 2  ·  Version 2
  Problem 1: Flip Game

  You are playing a Flip Game with your friend.

  You are given a string `currentState` that contains only `'+'` and `'-'`.
  You and your friend take turns to flip **two consecutive** `"++"` into
  `"--"`. The game ends when a person can no longer make a move, and
  therefore the other person will be the winner.

  Return all possible states of the string `currentState` after **one valid
  move**. You may return the answer in **any order**. If there is no valid
  move, return an empty list `[]`.

  Write your solution for `generate_possible_next_moves` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `generate_possible_next_moves` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def generate_possible_next_moves(current_state):
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

grade(generate_possible_next_moves)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('++++', expected=['--++', '+--+', '++--'])   # checks the value your code returns against this example
