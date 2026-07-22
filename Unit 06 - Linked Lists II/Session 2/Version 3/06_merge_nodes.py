'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 2  ·  Version 3
  Problem 6: Merge Nodes Between Zeros

  Given the head of a linked list which contains a series of integers
  separated by 0s, merge the nodes lying between two zero nodes into a
  single node whose value is the sum of all the merged nodes. The modified
  list should not contain any zeroes. The head and tail of the list will be
  nodes with value zero. Return the head of the merged list.

  Evaluate the time and space complexity of your solution. Define your
  variables and provide a rationale for why you believe your solution has
  the stated time and space complexity.

  Write your solution for `merge_nodes` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `merge_nodes` and its parameters exactly as given —
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



def merge_nodes(head):
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

grade(merge_nodes)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([0, 3, 1, 0, 4, 5, 2, 0], expected=[4, 11])   # checks the value your code returns against this example
