'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 2  ·  Version 1
  Problem 5: Merge Sort I

  Merge sort is a sorting algorithm that takes in an unsorted list and
  returns a sorted list in `O(n log n)` time which is faster than many other
  sorting algorithms that have `O(n²)` time complexity. It uses a divide and
  conquer approach.

  Merge sort works by using a divide and conquer approach: it divides the
  array into two halves until each sublist contains only a single element,
  then it recursively sorts each sublist, and merges the sorted sublists
  into a sorted array.

  Given the pseudo-code and helper function `merge()` below, implement the
  `merge_sort()` function.

  Write your solution for `merge_sort` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `merge_sort` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def merge_sort(lst):
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

grade(merge_sort)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([5, 3, 4, 2, 1], expected=[1, 2, 3, 4, 5])   # checks the value your code returns against this example
