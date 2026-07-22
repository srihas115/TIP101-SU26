'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 2  ·  Version 2
    Problem 4: Special Numbers

    You are given a sorted list of non-negative integers `nums`. `nums` is
    considered **special** if there exists a number `x` such that there are
    **exactly** `x` numbers in `nums` that are **greater than or equal to**
    `x`.

    Notice that `x` **does not** have to be an element in `nums`.

    Return `x` *if the array is **special**, otherwise, return* `-1`. It can
    be proven that if `nums` is special, the value for `x` is **unique**.

    Write your solution for `is_special` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `is_special` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def is_special(nums):
    pass

# Example Input: nums = [3,5]


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

grade(is_special)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, 5], expected=2)   # checks the value your code returns against this example
