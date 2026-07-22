'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 1  ·  Version 3
  Problem 1: In The Stars

  A recursive function is a function that calls itself within the body of
  the function.

  Step 1: Copy the recursive function `insert_stars()` into your IDE and run
  it.

  Step 2: Then create another function `insert_stars_iterative()` that
  produces the same output without using recursion or the built-in `join()`
  method.

  Compare your iterative (non-recursive) solution to the recursive solution
  provided. What is similar? What is different?

  Write your solution for `insert_stars_iterative` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `insert_stars_iterative` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def insert_stars(s):
    # If the string is empty or has only one character, return it as is
    if len(s) <= 1:
        return s
    # Otherwise, insert '*' between the first character and the rest, then recurse
    else:
        return s[0] + '*' + insert_stars(s[1:])

insert_stars('abc')


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

grade(insert_stars_iterative)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('abc', expected='a*b*c')   # checks the value your code returns against this example
