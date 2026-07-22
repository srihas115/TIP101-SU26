'''
==============================================================================
    Unit 10: Review  ·  Session 1  ·  Version 3
    Problem 5: Two Sum II

    Given an array of integers `numbers` that is sorted in **non-decreasing
    order**.

    Return the indices (**0-indexed**) of two numbers, `[index1, index2]`,
    such that they add up to a given target number `target` and `index1 <
    index2`. Note that `index1` and `index2` cannot be equal, therefore you
    may not use the same element twice.

    There will always be **exactly one valid solution**. Your solution must
    use `O(1)` additional space.

    Write your solution for `two_sum` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `two_sum` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def two_sum(numbers, target):
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

grade(two_sum)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], 3, expected=[0, 1])   # checks the value your code returns against this example
