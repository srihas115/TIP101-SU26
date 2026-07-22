'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 1  ·  Version 2
  Problem 6: Rock, Paper, Scissors

  Write a function `rock_paper_scissors()` that determines the winner of a
  game of Rock, Paper, Scissors. The function accepts two strings as
  parameters: `player1` and `player2`. Each parameter can have a value of
  `"rock"`, `"paper"`, or `"scissors"`.

  Print either `"Player 1 wins!"` or `"Player 2 wins!"` according to the
  following rules: Rock wins against scissors. Scissors wins against paper.
  Paper wins against rock.

  If both `player1` and `player2` have the same value, print `"It's a
  tie!"`.

  Write your solution for `rock_paper_scissors` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `rock_paper_scissors` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def rock_paper_scissors(player1, player2):
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

grade(rock_paper_scissors)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('rock', 'rock', expected="It's a tie!")   # checks the printed output against this example
