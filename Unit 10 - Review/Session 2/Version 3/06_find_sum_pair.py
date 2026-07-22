'''
==============================================================================
    Unit 10: Review  ·  Session 2  ·  Version 3
    Problem 6: Find Sum Pair

    Given a list of integers `numbers`, return the list of four integers in
    the list, `a`, `b`, `c`, and `d`, such that `a + b = c + d`. You may
    return the numbers in any order. If no such integers exist, return an
    empty list.

    Write your solution for `find_sum_pair` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `find_sum_pair` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_sum_pair(numbers):
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
from problem_set_solution_validator import grade

grade(find_sum_pair)   # ▶ Run this file to validate your solution
