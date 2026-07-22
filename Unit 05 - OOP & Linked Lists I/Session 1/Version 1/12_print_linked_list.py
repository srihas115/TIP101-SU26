'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 1
  Problem 12: Printing Linked List

  Write a function `print_linked_list()` that takes in a head node as a
  parameter and prints the linked list using the string `" -> "` to separate
  each node.

  *Note: The "head" of a linked list is the first element in the linked
  list, equivalent to `lst[0]` of a normal list.*

  Write your solution for `print_linked_list` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `print_linked_list` and its parameters exactly as given —
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



def print_linked_list(head):
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

grade(print_linked_list)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4, 5], expected='1 -> 2 -> 3 -> 4 -> 5')   # checks the printed output against this example
