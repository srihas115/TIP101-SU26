'''
==============================================================================
    Unit 10: Review  ·  Session 2  ·  Version 1
    Problem 3: GCD of Strings

    For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s =
    t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or
    more times).

    Given two strings `str1` and `str2`, return *the largest string* `x` *such
    that* `x` *divides both* `str1` *and* `str2`.

    Write your solution for `gcd_of_stings` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `gcd_of_stings` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def gcd_of_stings(str1, str2):
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

grade(gcd_of_stings)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('ABCABC', 'ABC', expected='ABC')   # checks the value your code returns against this example
