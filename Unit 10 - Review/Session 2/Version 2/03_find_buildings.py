'''
==============================================================================
    Unit 10: Review  ·  Session 2  ·  Version 2
    Problem 3: Buildings with an Ocean View

    There are `n` buildings in a line. You are given an list of integers
    `heights` of size `n` that represents the heights of the buildings in the
    line.

    The ocean is to the right of the buildings. A building has an ocean view
    if the building can see the ocean without obstructions. Formally, a
    building has an ocean view if all the buildings to its right have a
    **smaller** height.

    Return a list of indices of buildings that have an ocean view, sorted in
    increasing order.

    Write your solution for `find_buildings` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `find_buildings` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_buildings(heights):
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

grade(find_buildings)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([4, 2, 3, 1], expected=[0, 2, 3])   # checks the value your code returns against this example
