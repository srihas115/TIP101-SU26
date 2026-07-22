'''
==============================================================================
    Unit 10: Review  ·  Session 1  ·  Version 1
    Problem 1: Valid Parentheses

    Given a string `s` containing just the characters `'('`, `')'`, `'{'`,
    `'}'`, `'['` and `']'`, return `True` if the input string is valid and
    `False` otherwise.

    An input string is valid if:

    1. Open brackets must be closed by the same type of brackets. 2. Open
    brackets must be closed in the correct order. 3. Every close bracket has a
    corresponding open bracket of the same type.

    Write your solution for `is_valid` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `is_valid` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def is_valid(s):
    pass

s = "()[]{}"

s = "(())"

s = "(]"

s = "([)]"


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

grade(is_valid)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('()', expected=True)   # checks the value your code returns against this example
