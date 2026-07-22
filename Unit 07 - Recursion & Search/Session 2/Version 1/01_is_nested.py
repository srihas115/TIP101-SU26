'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 2  ·  Version 1
    Problem 1: Neatly Nested

    Given a string, return `True` if it is a nesting of zero or more pairs of
    parentheses. Return `False` otherwise. A valid pair of parentheses is
    defined as `()`. The input string will only contain the characters `(` or
    `)`. Your solution must be recursive.

    Evaluate the time and space complexity of your solution.

    Write your solution for `is_nested` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `is_nested` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:
((())) --> empty
(

'''


def is_nested(s):
    if s == "":
        return True
    if s[0] == "(" and s[-1] == ")":
        return is_nested(s[1:-1])
    return False

# Example Input: "(())"
example = "(())"
print(is_nested(example))


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

grade(is_nested)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('(())', expected=True)   # checks the value your code returns against this example
