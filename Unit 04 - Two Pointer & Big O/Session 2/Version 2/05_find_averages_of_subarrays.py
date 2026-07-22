'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 2
  Problem 5: Averages of Subarray

  The **sliding window technique** is an algorithmic technique often used to
  find a subarray or substring that meets certain criteria. It works by
  initializing two pointers to point at the start and end of a ‘window’ or
  subsection of the string/array at a time. The pointers are then
  incremented to slide the window and examine a different subarray or
  substring.

  Use the sliding window technique to solve the following problem:

  Write a function `find_averages_of_subarrays()` that takes in a list of
  integers `nums` and an integer `k` as parameters. The function returns a
  list where each element in the average of each contiguous subarray of size
  `k` in `nums` where `1 ≤k ≤ len(nums)`

  Write your solution for `find_averages_of_subarrays` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_averages_of_subarrays` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_averages_of_subarrays(k, nums):
    pass  # replace this line with your solution













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

grade(find_averages_of_subarrays)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(5, [1, 3, 2, 6, -1, 4, 1, 8, 2], expected=[2.2, 2.8, 2.4, 3.6, 2.8])   # checks the value your code returns against this example
