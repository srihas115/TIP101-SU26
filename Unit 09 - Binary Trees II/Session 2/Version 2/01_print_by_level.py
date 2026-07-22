'''
==============================================================================
  Unit 9: Binary Trees II  ·  Session 2  ·  Version 2
  Problem 1: Print Level Order

  Given the following pseudocode and the root of a binary tree, print the
  level order traversal of it’s nodes’ values (i.e., from left to right,
  level by level).

  Evaluate the time complexity of your solution. Define your variables and
  give a rationale as to why you believe your solution has the stated time
  complexity.

  Write your solution for `print_by_level` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `print_by_level` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


from collections import deque # This is a popular library used for queues

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_by_level(root):
    # If the tree is empty:
    # return

    # Create an empty queue using deque

    # Add the root to the queue

    # While the queue is not empty:
    # Pop the next node off the queue (pop from the left side!)
    # Print the popped node

    # Add each of the popped node's children to the end of the queue
    pass


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

grade(print_by_level)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([4, 2, 6, 1, 3], expected='4\n2\n6\n1\n3')   # checks the printed output against this example
