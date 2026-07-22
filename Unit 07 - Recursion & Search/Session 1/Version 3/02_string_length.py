'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 1  ·  Version 3
    Problem 2: String Length Cases

    Given the base case and recursive case, write a recursive function
    `string_length()` that returns the length of a string `s` without using
    the built-in `len()` function.

    **Base Case:** An empty string should have size `0`.

    **Recursive Case:** We can restate the problem to say that the string
    length is `1` `+` the length of `s[1:]`.

    Write your solution for `string_length` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `string_length` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def string_length(s):
    pass

# Example Input: 'abc'


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

grade(string_length)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('abc', expected=3)   # checks the value your code returns against this example
