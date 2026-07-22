'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 1  ·  Version 1
    Problem 1: Hello Hello

    A recursive function is a function that calls itself within the body of
    the function.

    Step 1: Copy the recursive function `repeat_hello()` into your IDE and run
    it.

    Step 2: Then create another function `repeat_hello_iterative()` that
    produces the same output without using recursion.

    Compare your iterative (non-recursive) solution to the recursive solution
    provided. What is similar? What is different?

    Write your solution for `repeat_hello_iterative` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `repeat_hello_iterative` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


# Time: O(n)
# Space: O(n)
def repeat_hello(n):
    if n > 0:
        print("Hello")
        repeat_hello(n - 1)

print("Recursive")
repeat_hello(5)

# Time: O(n)
# Space: O(1)
def repeat_hello_iterative(n):
    for i in range(n):
        print("Hello")

print("Iterative")     
repeat_hello_iterative(5)


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

grade(repeat_hello_iterative)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(5, expected='Hello\nHello\nHello\nHello\nHello')   # checks the printed output against this example
