'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 2  ·  Version 2
    Problem 1: Substring Search

    Given two strings `s` and `sub`, write a function `count_substring()` that
    returns the number of times the substring `sub` occurs in `s`. Occurrences
    should not overlap. A substring is a sequence of adjacent characters
    within a larger string.

    Your solution must be recursive.

    Evaluate the time complexity of your solution.

    Write your solution for `count_substring` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `count_substring` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def count_substring(s, sub):
    pass

# Example Input: s = "abcdeabcde" sub = "abc"


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

grade(count_substring)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('abcdeabcde', 'abc', expected=2)   # checks the value your code returns against this example
