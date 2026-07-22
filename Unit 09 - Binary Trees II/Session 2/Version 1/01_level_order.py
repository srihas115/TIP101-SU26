'''
==============================================================================
  Unit 9: Binary Trees II  ·  Session 2  ·  Version 1
  Problem 1: Level Order Traversal

  Given the following pseudocode and the `root` of a binary tree, return a
  list of the level order traversal of it’s nodes’ values (i.e., from left
  to right, level by level).

  Evaluate the time complexity of your solution. Define your variables and
  give a rationale as to why you believe your solution has the stated time
  complexity.

  Write your solution for `level_order` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `level_order` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    # If the tree is empty:
    # return an empty list

    # Create an empty queue using deque
    # Create an empty list to store the explored nodes

    # Add the root to the queue

    # While the queue is not empty:
    # Pop the next node off the queue (pop from the left side!)
    # Add the popped node to the list of explored nodes

    # Add each of the popped node's children to the end of the queue

    # Return the list of visited nodes
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

grade(level_order)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([4, 2, 6, 1, 3], expected=[4, 2, 6, 1, 3])   # checks the value your code returns against this example
