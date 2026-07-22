'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 2  ·  Version 2
  Problem 5: Merge Sort II

  Merge sort is a sorting algorithm that takes in an unsorted list and
  returns a sorted list in `O(n log n)` time which is faster than many other
  sorting algorithms that have `O(n²)` time complexity. It uses a divide and
  conquer approach.

  Merge sort works by using a divide and conquer approach: it divides the
  array into two halves until each sublist contains only a single element,
  then it recursively sorts each sublist, and merges the sorted sublists
  into a sorted array.

  Given the main function `merge_sort()` below, implement the helper
  function `merge()` below. `merge()` accepts two sorted lists `left` and
  `right` and returns a sorted list.

  Write your solution for `merge` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `merge` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def merge_sort(lst):
        # If the length of the list is 0-1, the list is already sorted.
    if len(lst) <= 1:
        return arr

    # Find the middle index of the array
    mid = len(arr) // 2
    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive calls to merge_sort for sorting the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted arrays
    return merge(left_half, right_half)

def merge(left, right):
    pass

# Example Input:  left = [1,3,5], right = [2,4]


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

grade(merge)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 3, 5], [2, 4], expected=[1, 2, 3, 4, 5])   # checks the value your code returns against this example
