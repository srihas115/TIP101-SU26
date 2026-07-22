class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_dict(root):
    # If the tree is empty:
    # return an empty dictionary

    # Create an empty dictionary
    # Create an empty queue using deque

    # Append a tuple (root, 1) to the queue. The queue will store tuples of (node, level)

    # While the queue is not empty:
    # Pop the next node, level pair off the queue (pop from the left side!)

    # If the level is not yet a key in the dictionary
    # Add to dictionary with empty list as a value

    # Add a tuple with each of the popped node's children
    # and incremented level to the end of the queue
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

grade(level_dict)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([4, 2, 6, 1, 3], expected={1: [4], 2: [2, 6], 3: [1, 3]})   # checks the value your code returns against this example
