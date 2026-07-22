'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 2
  Problem 1: Merge Sorted Lists

  The **two-pointer approach** is a common technique in which we initialize
  two variables (also called a pointer in this context) to track different
  indices or places in a list or string, then moves the pointers to point at
  new indices based on certain conditions. A common variation of this
  technique is to point one variable at the beginning of one list/string and
  a second pointer at the beginning of a second list/string, then increment
  each pointer conditionally to solve a problem.

  Using the two pointer approach, write a function `merge_sorted_lists()`
  that takes in two sorted lists `lst1` and `lst2` as parameters and merges
  them into a single sorted list. The function returns the new list.

  Write your solution for `merge_sorted_lists` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `merge_sorted_lists` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def merge_sorted_lists(lst1, lst2):
    pass

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
merged_lst = merge_sorted_lists(lst1, lst2)
print(merged_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - both lists empty")
print("  expected:", [], "| got:", merge_sorted_lists([], []))

print("Test 2 - one list empty")
print("  expected:", [1,2,3], "| got:", merge_sorted_lists([1,2,3], []))

print("Test 3 - duplicate values across lists")
print("  expected:", [1,1,2,2], "| got:", merge_sorted_lists([1,2], [1,2]))

print("Test 4 - single-element lists")
print("  expected:", [3,5], "| got:", merge_sorted_lists([5], [3]))


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

grade(merge_sorted_lists)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 3, 5], [2, 4, 6], expected=[1, 2, 3, 4, 5, 6])   # checks the value your code returns against this example
