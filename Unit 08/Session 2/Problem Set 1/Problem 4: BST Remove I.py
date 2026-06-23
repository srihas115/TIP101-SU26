"""Problem 4: BST Remove I

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
# Expected Output: 13
# Expected Output Tree:
#
# 13
# / \
# / \
# 5 15
# / \ \
# 1 8 16
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
