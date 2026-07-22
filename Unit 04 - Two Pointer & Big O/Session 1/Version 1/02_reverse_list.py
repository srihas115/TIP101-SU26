'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 1
  Problem 2: Two-Pointer Reverse List

  Write a function `reverse_list()` that takes in a list `lst` and returns
  elements of the list in reverse order. The list should be reversed *in-
  place* without using list slicing (e.g. `lst[::-1]`).

  Instead, use the **two-pointer approach**, which is a common technique in
  which we initialize two variables (also called a pointer in this context)
  to track different indices or places in a list or string, then moves the
  pointers to point at new indices based on certain conditions. In the most
  common variation of the two-pointer approach, we initialize one variable
  to point at the beginning of a list and a second variable/pointer to point
  at the end of list. We then shift the pointers to move inwards through the
  list towards each other, until our problem is solved or the pointers reach
  the opposite ends of the list.

  Write your solution for `reverse_list` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `reverse_list` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def reverse_list(lst):
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

grade(reverse_list)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4, 5], expected=[5, 4, 3, 2, 1])   # checks the value your code returns against this example
