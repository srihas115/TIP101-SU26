'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 2  ·  Version 1
  Problem 5: Add Two Numbers

  You are given two non-empty linked lists representing two non-negative
  integers. The digits are stored in reverse order, and each of their nodes
  contains a single digit. Add the two numbers and return the sum as a
  linked list.

  Write your solution for `add_two_numbers` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `add_two_numbers` and its parameters exactly as given —
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



def add_two_numbers(head_a, head_b):
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

grade(add_two_numbers)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([2, 4, 3], [5, 6, 4], expected=[7, 0, 8])   # checks the value your code returns against this example
