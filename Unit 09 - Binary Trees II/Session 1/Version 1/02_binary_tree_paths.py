'''
==============================================================================
    Unit 9: Binary Trees II  ·  Session 1  ·  Version 1
    Problem 2: Root-to-Leaf Paths

    Given the `root` of a binary tree, return a list of *all root-to-leaf
    paths in **any order***.

    A **leaf** is a node with no children.

    Evaluate the time complexity of your function.

    Write your solution for `binary_tree_paths` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `binary_tree_paths` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_paths(root):
    paths = []

    if root is None:
        return paths

    helper(root, str(root.val), paths)
    return paths

def helper(node, path, paths):
    if node.left is None and node.right is None:
        paths.append(path)
        return

    if node.left is not None:
        helper(node.left, path + "->" + str(node.left.val), paths)
    if node.right is not None:
        helper(node.right, path + "->" + str(node.right.val), paths)


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

grade(binary_tree_paths)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, None, 5], expected=['1->2->5', '1->3'])   # checks the value your code returns against this example
