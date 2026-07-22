'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 2  ·  Version 1
  Problem 4: Convert Binary Linked List to Integer

  You are given the head of a linked list. Each value in the linked list is
  either 0 or 1, and the entire linked list represents a binary number.
  Return an integer that is the decimal value of the number represented by
  the linked list. The most significant bit is at the head of the linked
  list.

  Write your solution for `binary_to_int` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `binary_to_int` and its parameters exactly as given —
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



def binary_to_int(head):
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

grade(binary_to_int)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 0, 1], expected=5)   # checks the value your code returns against this example
