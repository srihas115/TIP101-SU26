'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 1  ·  Version 2
    Problem 2: Fibonacci Cases

    Given the base case and recursive case, write a function `fibonacci()`
    that returns the `nth` number in the `fibonacci` sequence. The Fibonacci
    sequence is a mathematical sequence of numbers where each number is the
    sum of the two preceding numbers.

    **Base Cases:** Because Fibonacci numbers are defined by adding the two
    previous numbers in the sequence, the first two Fibonacci numbers are pre-
    defined. By definition, the 0th Fibonacci number is `0`, and the 1st
    Fibonacci number is `1`.

    **Recursive Case:** The `nth` Fibonacci number is the `n-1th` Fibonacci
    number `+` the `n-2th` Fibonacci number.

    Write your solution for `fibonacci` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `fibonacci` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def fibonacci(n):
    pass

# Example Input: 6


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

grade(fibonacci)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(6, expected=8)   # checks the value your code returns against this example
