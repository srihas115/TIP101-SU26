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
# Complete the 'remove_node' function below.
#
# The function is expected to return a TreeNode.
# The function accepts following parameters:
#  1. TreeNode root
#  2. INTEGER value
#

def remove_node(root, value):
    # Write your code here
    pass

if __name__ == '__main__':
    def tree_to_tuple(root):
        if root is None:
            return None
        return (root.val, tree_to_tuple(root.left), tree_to_tuple(root.right))

    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7))
    print("remove_node(root, 3) ->", tree_to_tuple(remove_node(root, 3)))
