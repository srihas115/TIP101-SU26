'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 2  ·  Version 2
  Problem 1: Convert to Circular Linked List

  A circular linked list is a linked list where the tail node points at the
  head node. Write a function that transforms a singly linked list into a
  circular linked list. Return the head of the linked list. Evaluate the
  time and space complexity of your solution. Define your variables and
  provide a rationale for why you believe your solution has the stated time
  and space complexity.

  Write your solution for `make_circular` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `make_circular` and its parameters exactly as given —
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



def make_circular(head):
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
from problem_set_solution_validator import grade

grade(make_circular)   # ▶ Run this file to validate your solution
