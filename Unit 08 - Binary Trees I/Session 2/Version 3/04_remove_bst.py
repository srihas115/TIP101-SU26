'''
==============================================================================
    Unit 8: Binary Trees I  ·  Session 2  ·  Version 3
    Problem 4: BST Remove III (merge)

    Use the provided pseudocode to solve the problem below. Given a `value`
    and the `root` of a binary search tree, remove the node with the given
    `value`. Return the `root` of the modified tree.

    If multiple nodes with the given `value` exist, remove the first node you
    find.

    If you need to remove a node with two children, use the deletion by
    merging strategy. When you delete by merging, you take the two subtrees of
    the given node and attach the root of the right subtree to the largest
    node in the left subtree.

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
        pass
def remove_bst(root, key):
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

grade(remove_bst)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([10, 5, 15, 1, 8, 13, 16], 10, expected=[5, 1, 8, None, None, None, 15, 13, 16])   # checks the value your code returns against this example
