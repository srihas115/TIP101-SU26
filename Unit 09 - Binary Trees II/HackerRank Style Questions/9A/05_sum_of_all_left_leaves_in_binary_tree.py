#!/bin/python3

import math
import os
import random
import re
import sys
import ast


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#
# Complete the 'sum_left_leaves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts TreeNode root as parameter.
#

def sum_left_leaves(root):
    # Write your code here
    if root is None:
        return 0

    total = 0

    def is_leaf(node):
        return node is not None and node.left is None and node.right is None

    def dfs(node):
        nonlocal total
        if node is None:
            return
        if is_leaf(node.left):
            total += node.left.val
        else:
            dfs(node.left)
        dfs(node.right)

    dfs(root)

    return total

if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("sum_left_leaves(root) ->", sum_left_leaves(root))
    print("sum_left_leaves(None) ->", sum_left_leaves(None))
