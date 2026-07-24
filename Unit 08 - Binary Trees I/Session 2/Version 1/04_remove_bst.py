'''
==============================================================================
    Unit 8: Binary Trees I  ·  Session 2  ·  Version 1
    Problem 4: BST Remove I

    Use the provided pseudocode to solve the problem below. Given a `key` and
    the `root` of a binary search tree, remove the node with the given `key`.
    Return the `root` of the modified tree.

    The tree is sorted by `key`. If multiple nodes with the given `key` exist,
    remove the first node you find. If you need to remove a node with two
    children, use the in-order successor of that node, which is the smallest
    value in its right subtree. You do not need to maintain a balanced tree.

    Evaluate the time complexity of your function.

    Write your solution for `remove_bst` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `remove_bst` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode():
    def __init__(self, key, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        

def remove_bst(root, key):
    if root is None:
        return None
    
    # Locate the node to be removed
    if key < root.key:
        root.left = remove_bst(root.left, key)
    elif key > root.key:
        root.right = remove_bst(root.right, key)
    else:
        # If the node is a leaf node:
        if root.left is None and root.right is None:
            return None
            # Remove the node by redirecting the appropriate child reference of its parent to None
    
        # If the node has one child:
            # Replace the node with its child, updating its parent's nodes child reference appropriately
    
    
        # If the node has two children:
        if root.left is not None and root.right is not None:
            # Find the node's inorder successor (smallest node in right subtree)
            # Swap the value of the node and its inorder successor
            # Recursively remove the successor (which now has the current node's value)
  
  
	# Return the root of the updated tree
    return root

# Example Input Tree #1: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16

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

grade(remove_bst)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([10, 5, 15, 1, 8, 13, 16], 10, expected=[13, 5, 15, 1, 8, None, 16])   # checks the value your code returns against this example
