'''
==============================================================================
    Unit 8: Binary Trees I  ·  Session 2  ·  Version 1
    Problem 3: BST Insert I

    Given the `root` of a binary search tree, insert a new node with a given
    `key` and `value` into the tree. Return the `root` of the modified tree.
    The tree is sorted by key. If a node with the given `key` already exists,
    update the the existing key’s value. You do not need to maintain a
    balanced tree.

    Evaluate the time complexity of your function.

    Write your solution for `insert` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `insert` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode():
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def insert(root, key, value):
    if root is None:  # base case
        return TreeNode(key, value)        

    if key == root.key:                                 # matched
        root.value = value
    elif key < root.key:                                # go to the left tree
        root.left = insert(root.left, key, value)
    else:                                               # go to the right tree
        root.right = insert(root.right, key, value)
    
    return root

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

grade(insert)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([10, 5, 15, 1, 6], 9, 'Naruto', expected=[10, 5, 15, 1, 6, None, None, None, None, None, 9])   # checks the value your code returns against this example
