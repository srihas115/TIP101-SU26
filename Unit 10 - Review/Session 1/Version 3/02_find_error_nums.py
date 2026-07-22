'''
==============================================================================
  Unit 10: Review  ·  Session 1  ·  Version 3
  Problem 2: Set Mismatch

  You have a set of integers `s`, which originally contains all the numbers
  from `1` to `n`. Unfortunately, due to some error, one of the numbers in
  `s` got duplicated to another number in the set, which results in
  **repetition of one** number and **loss of another** number.

  You are given a list of integers `nums` representing the data status of
  this set after the error.

  Find the number that occurs twice and the number that is missing and
  return *them in the form of a list*.

  Write your solution for `find_error_nums` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_error_nums` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_error_nums(nums):
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

grade(find_error_nums)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 2, 4], expected=[2, 3])   # checks the value your code returns against this example
