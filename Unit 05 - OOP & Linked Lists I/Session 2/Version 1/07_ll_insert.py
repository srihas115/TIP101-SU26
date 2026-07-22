'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 1
  Problem 7: Insert Value

  Write a function `ll_insert()` that takes in a `head` of a linked list, a
  value `val`, and an index `i` as parameters.

  The function should insert a new `Node` with value `val` at index `i` of
  the linked list, then return the head of the linked list. - If `i` is
  greater than the length of the list, insert the new node at the end of the
  list.

  *Hint: Linked lists do not have built-in indices so you will need to track
  the indices yourself.*

  Write a helper function to help you print the new list!

  Write your solution for `ll_insert` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `ll_insert` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



def ll_insert(head, val, i):
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

grade(ll_insert)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([3, 8, 12, 9], 20, 2, expected=[3, 8, 20, 12, 9])   # checks the value your code returns against this example
