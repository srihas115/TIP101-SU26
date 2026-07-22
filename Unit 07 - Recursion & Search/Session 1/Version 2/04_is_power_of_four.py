'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 1  ·  Version 2
    Problem 4: Recursive Power of 4

    Given an integer `n`, return `True` if `n` is a power of four. Otherwise,
    return `False`.

    An integer `n` is a power of four if there exists an integer `x` such that
    `n == 4ˣ`.

    Solve the problem recursively. What is the time complexity of this
    function? What is the space complexity?

    Write your solution for `is_power_of_four` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `is_power_of_four` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def is_power_of_four(n):
    pass

# Example Input 1: 16

# Example Input 2: 8


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

grade(is_power_of_four)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(16, expected=True)   # checks the value your code returns against this example
