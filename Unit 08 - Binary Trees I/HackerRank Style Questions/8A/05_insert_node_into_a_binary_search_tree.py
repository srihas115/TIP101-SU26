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
# Complete the 'insert_node' function below.
#
# The function is expected to return a TreeNode.
# The function accepts following parameters:
#  1. TreeNode root
#  2. INTEGER val
#

'''
Understand:
    input: (TreeNode) root of the tree, (int) value to be inserted
    output: (TreeNode) the root again
    base case: there is no node

Match:
    this is a BST traversal problem
    we can user recursion to decide if we want to go left or right

Plan:
    first check the base case if there is no node
        return a treenode with the val
    if val is greater than root
        root.right's value is insert_node(root.left, val)
    else if val is less than root
        root.left's value is insert_node(root.right, val)

    return root

'''

def insert_node(root, val):
    # Write your code here
    pass

if __name__ == '__main__':
    def tree_to_tuple(root):
        if root is None:
            return None
        return (root.val, tree_to_tuple(root.left), tree_to_tuple(root.right))

    root = TreeNode(4, TreeNode(2), TreeNode(7))
    print("insert_node(root, 5) ->", tree_to_tuple(insert_node(root, 5)))
