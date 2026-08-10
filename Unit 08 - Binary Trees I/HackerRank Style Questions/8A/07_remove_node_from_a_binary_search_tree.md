# Remove Node from a Binary Search Tree

Source: HackerRank Style Unit 8 Assessment, Version A

## Question

Given the root of a binary search tree, remove the node with the value val into the tree. All nodes in the
tree are guaranteed to be unique. Return the root.
If you need to replace a parent node with two children, use the in-order successor of that node, such that
replacement.val is the smallest value greater than removed.val
# Example Input Tree:
#       7
#      / \
#     3  10
#        / \
#       8  12
# Input: root = 7, val = 10
# Expected Output: root = 7
# Expected output tree:
#       7
#      / \
#     3   12
#        /
#       8
#
# Note: In-order successor of 10 is 12
