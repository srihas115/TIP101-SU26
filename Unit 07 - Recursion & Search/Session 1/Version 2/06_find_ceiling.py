'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 1  ·  Version 2
    Problem 6: Find Ceiling

    Given a sorted list of integers and a value x, return the index of the
    ceiling of x. The ceiling of x is the smallest element in the array larger
    than or equal to x. If there is no ceiling of x, return -1.

    Evaluate the time and space complexity of your function.

    Write your solution for `find_ceiling` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `find_ceiling` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_ceiling(lst, x):
    pass

# Example Input: lst = [1, 2, 8, 10, 11, 12, 19], x = 5


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

grade(find_ceiling)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 8, 10, 11, 12, 19], 5, expected=2)   # checks the value your code returns against this example
