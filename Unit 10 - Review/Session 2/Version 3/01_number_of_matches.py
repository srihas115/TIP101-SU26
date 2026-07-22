'''
==============================================================================
    Unit 10: Review  ·  Session 2  ·  Version 3
    Problem 1: Count of Matches in Tournament

    You are given an integer `n`, the number of teams in a tournament that has
    strange rules:

    - If the current number of teams is **even**, each team gets paired with
    another team. A total of `n / 2` matches are played, and `n / 2` teams
    advance to the next round. - If the current number of teams is **odd**,
    one team randomly advances in the tournament, and the rest gets paired. A
    total of `(n - 1) / 2` matches are played, and `(n - 1) / 2 + 1` teams
    advance to the next round.

    Return *the number of matches played in the tournament until a winner is
    decided.*

    Write your solution for `number_of_matches` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `number_of_matches` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def number_of_matches(n):
    pass


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

grade(number_of_matches)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(7, expected=6)   # checks the value your code returns against this example
