"""Problem 2: Find Lonely Nodes

Solution intentionally left blank for practice.
"""

class TreeNode:
    pass

    def __init__(self, val=0, left=None, right=None):
        pass

def find_lonely_nodes(root):
    pass

# Example usage / test cases from the prompt:
# Example Input Tree #1:
#
# 1
# / \
# 2 3
# \
# 4
#
# Input: root = 1
# Expected Output: [4]
# Explanation: Node 4 is the only lonely node.
# Node 1 is the root and is not lonely
# Node 2 and 3 have the same parent and are not lonely
#
# Example Input Tree #2:
#
# 7
# / \
# 1 4
# / / \
# 6 5 3
# \
# 2
#
# Input: root = 7
# Expected Output: [6,2]
# [2,6] is also an acceptable answer
#
# Example Input Tree #3:
#
# 11
# / \
# 99 88
# / \
# 77 66
# / \
# 55 44
# / \
# 33 22
#
# Input: root = 11
# Expected Output: [77, 55, 33, 66, 44, 22]
# List elements may be returned in any order
# Explanation: Nodes 99 and 88 share the same parent. Node 11 is the root.
# All other nodes are lonely.
