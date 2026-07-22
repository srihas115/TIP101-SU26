'''
==============================================================================
    Unit 8: Binary Trees I  ·  Session 1  ·  Version 1
    Problem 3: 3-Node Sum II

    Given the `root` of a binary tree that has at most `3` nodes: the root,
    its left child, and its right child, return `True` if the value of the
    root is equal to the sum of the values of its two children. Return `False`
    otherwise.

    Evaluate the time complexity of your function.

    Write your solution for `check_tree` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `check_tree` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    if root is None:  # if tree is empty
        return False
    # if left child is equal to the root and there is only 1 child
    elif (root.right is None) and (root.left) and (root.val == root.left.val):
        return True
    # if right child is equal to the root and there is only 1 child
    elif (root.left is None) and (root.right) and (root.val == root.right.val):
        return True
    # check if the sum of both children is equal to the root
    elif root.left and root.right and root.val == root.left.val + root.right.val:
        return True
    return False
    
# Test Cases:
tree1 = TreeNode(10, TreeNode(10), None)  # only one child
tree2 = TreeNode(5, TreeNode(3), TreeNode(2))
tree3 = TreeNode(5, None, TreeNode(2))
tree4 = TreeNode(None)

print(check_tree(tree1))
print(check_tree(tree2))
print(check_tree(tree3))
print(check_tree(tree4))


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

grade(check_tree)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([10, 10], expected=True)   # checks the value your code returns against this example
