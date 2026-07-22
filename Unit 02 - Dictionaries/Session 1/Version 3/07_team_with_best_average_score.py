'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 3
  Problem 7: Best Team

  You're developing an analytics tool for a sports league. Your task is to
  write a function named `team_with_best_average_score()` that returns the
  team with the highest average score over a season.

  The function should accept a list of dictionaries named `games` as a
  parameter. Each dictionary represents data from a game, including the
  `"team_name"`, and the `"score"` they achieved in that game. The function
  calculates the average score for each team across all games and returns
  the team with the highest average score.

  Write your solution for `team_with_best_average_score` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `team_with_best_average_score` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def team_with_best_average_score(games):
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

grade(team_with_best_average_score)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([{'team_name': 'Lions', 'score': 23}, {'team_name': 'Tigers', 'score': 30}, {'team_name': 'Lions', 'score': 27}, {'team_name': 'Bears', 'score': 20}, {'team_name': 'Tigers', 'score': 24}, {'team_name': 'Bears', 'score': 22}], expected='Tigers')   # checks the value your code returns against this example
