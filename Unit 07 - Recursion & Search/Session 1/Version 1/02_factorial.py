'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 1  ·  Version 1
    Problem 2: Factorial Cases

    Given the base case and recursive case, write a function `factorial()`
    that returns the factorial of a non-negative integer `n`. The factorial of
    a number is the product of all numbers between 1 and `n`.

    **Base Case:** The smallest number we can find a factorial of is `0`. By
    definition, the factorial of `0` is `1`.

    **Recursive Case:** We can restate the problem to say that the factorial
    of `n` is `n` * the factorial of `n-1`.

    Write your solution for `factorial` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `factorial` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


# Time: O(n) because n recursive calls before hitting the base case
# Space: O(n) because n stack frames alive simultaneously since each call is waiting on n * factorial(n-1) to return before it can multiply and return itself
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    
print(factorial(5))
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

grade(factorial)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(5, expected=120)   # checks the value your code returns against this example
