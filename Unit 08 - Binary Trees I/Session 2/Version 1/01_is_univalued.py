'''
==============================================================================
    Unit 8: Binary Trees I  ·  Session 2  ·  Version 1
    Problem 1: Is Uni-valued

    A binary tree is uni-valued if every node in the tree has the same value.
    Given the `root` of a binary tree, return `True` if the given tree is uni-
    valued and `False` otherwise.

    Evaluate the time complexity of your solution.

    Write your solution for `is_univalued` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `is_univalued` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

# with sets
def is_univalued2(root):
    if root is None:
        return True
        
    counter = set()
    def helper(root, counter):
        if root is None:
            return False
        if len(counter) >= 2:
            return False
        
        is_univalued(root.left)
        counter.add(root.value)
        is_univalued(root.right)

    return True


# recursive
# Time: O(n)
# Space: O(n)
def is_univalued(root):
    if root is None:  # base case
        return True
    
    if root.left is not None and root.left.val != root.val:
        return False
    if root.right is not None and root.right.val != root.val:
        return False
    
    return is_univalued(root.left) and is_univalued(root.right)

example1 = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
print(is_univalued(example1))

example2 = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(2, None, TreeNode(1)))
print(is_univalued(example2))


#
#     1   
#    / \
#  True True
# 

#       1 
#      /  \
#     1    T
#         /  \
#        T    T


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

grade(is_univalued)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 1, 1, 1, 1, None, 1], expected=True)   # checks the value your code returns against this example
