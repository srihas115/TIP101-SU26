'''
==============================================================================
    Unit 10: Review  ·  Session 2  ·  Version 2
    Problem 6: Sequential Digits

    An integer has *sequential digits* if and only if each digit in the number
    is one more than the previous digit.

    Return a **sorted** list of all the integers in the range `[low, high]`
    inclusive that have sequential digits.

    Write your solution for `sequential_digits` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `sequential_digits` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def sequential_digits(low, high):
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

grade(sequential_digits)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(100, 300, expected=[123, 234])   # checks the value your code returns against this example
