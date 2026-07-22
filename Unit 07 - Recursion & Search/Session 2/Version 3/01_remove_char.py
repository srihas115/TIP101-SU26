'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 2  ·  Version 3
    Problem 1: Recursive Remove Char

    Given a string `s` and a single character `char`, write a function
    `remove_char()` that recursively removes all instances of `char` from `s`
    and returns the new string.

    Evaluate the time complexity of your solution.

    Write your solution for `remove_char` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `remove_char` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def remove_char(s, char):
    pass

# Example Input: s = "xaxbxc", char = 'x'


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

grade(remove_char)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('xaxbxc', 'x', expected='abc')   # checks the value your code returns against this example
