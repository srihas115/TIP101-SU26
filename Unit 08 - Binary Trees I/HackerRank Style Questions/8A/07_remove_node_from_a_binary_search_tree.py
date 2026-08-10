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
    parent = None
    curr = root

    while curr is not None and curr.val != value:
        parent = curr
        if value < curr.val:
            curr = curr.left
        elif value > curr.val:
            curr = curr.right


    if curr is None:
        return root

    if curr.left and curr.right:
        succ_parent = curr
        succ = curr.right
        while succ.left is not None:
            succ_parent = succ
            succ = succ.left

        if succ_parent.left == succ:
            succ_parent.left = succ.right
        else:
            succ_parent.right = succ.right

        succ.left = curr.left
        succ.right = curr.right
        replace = succ
    else:
        replace = curr.left if curr.left is not None else curr.right


    if parent is None:
        root = replace
    elif parent.left is curr:
        parent.left = replace
    else:
        parent.right = replace

    return root

if __name__ == '__main__':
    def tree_to_tuple(root):
        if root is None:
            return None
        return (root.val, tree_to_tuple(root.left), tree_to_tuple(root.right))

    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7))
    print("remove_node(root, 3) ->", tree_to_tuple(remove_node(root, 3)))
