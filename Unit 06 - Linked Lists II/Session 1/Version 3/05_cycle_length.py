'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 1  ·  Version 3
  Problem 5: Are We There Yet?

  Given the head of a linked list, return the length of its cycle. A linked
  list has a cycle if at some point in the list, the node’s next pointer
  points back to a previous node in the list.

  Evaluate the time and space complexity of your solution. Define your
  variables and provide a rationale for why you believe your solution has
  the stated time and space complexity.

  Write your solution for `cycle_length` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `cycle_length` and its parameters exactly as given —
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



def cycle_length(head):
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

grade(cycle_length)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([[1, 2, 3, 4], 1], expected=3)   # checks the value your code returns against this example
