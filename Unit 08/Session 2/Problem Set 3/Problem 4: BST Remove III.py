"""Problem 4: BST Remove III

Solution intentionally left blank for practice.
"""

class TreeNode():
    pass

    def __init__(self, key, value, left=None, right=None):
        pass

def remove_bst(root, key):
    pass

# Example usage / test cases from the prompt:
# Example Input Tree #1: (tree depicted using keys)
#
# 10
# / \
# / \
# 5 15
# / \ / \
# 1 8 13 16
#
# Input: root = 10, key = 10
# Expected Output: 5
# Expected Output Tree:
#
# 5
# / \
# 1 8
# \
# 15
# / \
# 13 16
#
# Explanation: Deleting 10 leaves you with two subtrees. The left subtree has root 5. The right subtree has root 15.
# 8 is the largest node in the left subtree, so it's right child becomes 15 which is the root of the right subtree.
#
# Example Input Tree #2: (tree depicted using keys)
#
# 10
# / \
# / \
# 5 15
# / \ / \
# 1 8 13 16
# \
# 9
#
# Input: root = 10, key = 8
# Expected Output: 10 (Should return a node object)
# Expected Output Tree
#
# 10
# / \
# / \
# 5 15
# / \ / \
# 1 9 13 16
#
# Example Input Tree #3: (tree depicted using keys)
#
# 10
# / \
# / \
# 5 15
# / \ / \
# 1 8 13 16
# \
# 9
#
# Input: root = 10, key = 9
# Expected Output: 10 (Should return a node object)
# Expected Output Tree
#
# 10
# / \
# / \
# 5 15
# / \ / \
# 1 8 13 16
