'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 1  ·  Version 2
    Problem 4: Sleep Assessment

    Write a function `sleep_assessment()` that takes in an integer parameter
    `hours` indicating the number of hours the user slept. If `hours` is less
    than 8, print `"Oof, go back to bed!"`. If `hours` is greater than or
    equal to 8 and less than or equal to 10, print `"You got a good night's
    rest!"`. If `hours` is greater than 10, print `"You're a sleep prodigy!"`.

    Write your solution for `sleep_assessment` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `sleep_assessment` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def sleep_assessment(hours):
    if hours < 8:
        print("Oof, go back to bed!")
    elif hours >= 8 and hours <= 10:
        print("You got a good night's rest!")
    elif hours > 10:
        print("You're a sleep prodigy!")

sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)


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

grade(sleep_assessment)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(10, expected="You got a good night's rest!")   # checks the printed output against this example
