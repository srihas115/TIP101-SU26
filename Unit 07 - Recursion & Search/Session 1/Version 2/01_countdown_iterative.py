'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 1  ·  Version 2
    Problem 1: Counting Down

    A recursive function is a function that calls itself within the body of
    the function.

    Step 1: Copy this code into your IDE and run it.

    Step 2: Then create another function `countdown_iterative()` that produces
    the same output without using recursion.

    Compare your iterative (non-recursive) solution to the recursive solution
    provided. What is similar? What is different?

    Write your solution for `countdown_iterative` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `countdown_iterative` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)

countdown(5)

# Example Input: 5


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

grade(countdown_iterative)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(5, expected='5\n4\n3\n2\n1')   # checks the printed output against this example
