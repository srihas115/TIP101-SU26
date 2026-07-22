'''
==============================================================================
    Unit 8: Binary Trees I  ·  Session 1  ·  Version 1
    Problem 5: Find Leftmost Node II

    If you implemented the previous `left_most()` function iteratively,
    implement it recursively. If you implemented it recursively, implement it
    iteratively.

    Evaluate the time complexity of the function.

    Write your solution for `left_most` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `left_most` and its parameters exactly as given —
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

def left_most(root):
    if root is None:
        return None

    while root.left is not None:
        root = root.left
    return root.val


# test cases
tree1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), 5)  # expected: 4
tree2 = TreeNode(1, None, TreeNode(2, 3, None))  # expected: 1
tree3 = TreeNode(None)  # expected: none
tree4 = TreeNode(1, None, TreeNode(5))  # expected: 1

print(left_most(tree1))
print(left_most(tree2))
print(left_most(tree3))
print(left_most(tree4))

# time complexity: O(n)
    # best case: O(1)
    # worst case: O(n)
# space complexity: O(1)


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

grade(left_most)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 5, 4, 3], expected=4)   # checks the value your code returns against this example
