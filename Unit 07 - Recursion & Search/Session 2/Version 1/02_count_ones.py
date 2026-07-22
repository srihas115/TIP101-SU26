'''
==============================================================================
  Unit 7: Recursion & Search  ·  Session 2  ·  Version 1
  Problem 2: How Many 1s

  Given a sorted list of integers containing only 0s and 1s, count the total
  number of 1’s in the array in `O(log n)` time.

  Write your solution for `count_ones` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `count_ones` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def count_ones_iterative(lst):
    left = 0
    right = len(lst) - 1
    first_1 = len(lst)

    while left <= right:
        middle = left + (right - left) // 2
        if lst[middle] == 1:
            first_1 = middle
            right = middle - 1
        else:
            left = middle + 1

    return len(lst) - first_1

def count_ones_recursive(lst, left=0, right=None):
    if right is None:
        right = len(lst) - 1

    if left > right:
        return 0  # no 1s found in this range

    middle = (left + right) // 2

    if lst[middle] == 1:
        # count 1s to the left of (and including) mid, plus everything right of mid
        return count_ones_recursive(lst, left, middle - 1) + (right - middle + 1)
    else:
        return count_ones_recursive(lst, middle + 1, right)

# Example Input: [0, 0, 0, 0, 1, 1, 1]
print(count_ones_iterative([0, 0, 0, 0, 1, 1, 1]))
print(count_ones_recursive([0, 0, 0, 0, 1, 1, 1]))


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

grade(count_ones)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([0, 0, 0, 0, 1, 1, 1], expected=3)   # checks the value your code returns against this example
