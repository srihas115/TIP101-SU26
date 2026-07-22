'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 2
  Problem 8: Find Middle Node

  Write a function `find_middle_node()` that takes in the `head` of a linked
  list and returns the "middle" node. - If the linked list has an even
  length and there are two "middle" nodes, return the first middle node. -
  (E.g., "1 -> 2 -> 3 -> 4" would return 2, not 3.)

  Write your solution for `find_middle_node` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_middle_node` and its parameters exactly as given —
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



def find_middle_node(head):
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

grade(find_middle_node)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4], expected=2)   # checks the value your code returns against this example
