"""Problem 5: Sum of Binary Tree Node Tilts

Solution intentionally left blank for practice.
"""

class TreeNode:
    pass

    def __init__(self, value=0, left=None, right=None):
        pass

def find_tilt(root):
    pass

# Example usage / test cases from the prompt:
# Example Input Tree #1:
#
# 1
# / \
# 2 3
#
# Input: root = 1
# Expected Output: 1
# Explanation
# Tilt of node 2: |0 - 0| = 0 (no children)
# Tilt of node 3 : |0-0| = 0 (no children)
# Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
# Sum of every tilt : 0 + 0 + 1 = 1
#
# Example Input Tree #2:
#
# 4
# / \
# 2 9
# / \ \
# 3 5 7
#
# Example Input: root = 4
# Expected Output: 15
# Tilt of node 3 : |0-0| = 0 (no children)
# Tilt of node 5 : |0-0| = 0 (no children)
# Tilt of node 7 : |0-0| = 0 (no children)
# Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
# Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
# Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
# Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15
