"""Problem 3: Path Sum in Binary Tree

Solution intentionally left blank for practice.
"""

class TreeNode:
    pass

    def __init__(self, val=0, left=None, right=None):
        pass

def has_path_sum(root, target_sum):
    pass

# Example usage / test cases from the prompt:
# Example Input Tree #1:
#
# 5
# / \
# 4 8
# / / \
# 11 13 4
# / \ \
# 7 2 1
#
# Input: root = 5, target_sum = 22
# Expected Output: True
# Explanation: The root to leaf path 5 -> 4 -> 11 -> 2 sums to 22.
#
# Example Input Tree #2:
#
# 1
# / \
# 2 3
#
# Input: root = 1 , target_sum = 5
# Expected Output: False
# Explanation: There two root-to-leaf paths in the tree:
# 1 -> 2: The sum is 3.
# 1 -> 3: The sum is 4.
# There is no root-to-leaf path with sum = 5.
