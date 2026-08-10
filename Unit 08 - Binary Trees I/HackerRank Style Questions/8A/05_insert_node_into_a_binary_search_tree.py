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
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert_node(root.right, val)
    elif val < root.val:
        root.left = insert_node(root.left, val)

    return root



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    def make_tree(tree_tup):
        if tree_tup is None:
            return None # Base case
        elif len(tree_tup) != 3:
            print("Invalid input: ", tree_tup)
            return None # Invalid case
        # Happy case
        return TreeNode(tree_tup[0], make_tree(tree_tup[1]), make_tree(tree_tup[2]))

    def unmake_tree(root):
        if root is None:
            return None
        return (root.val, unmake_tree(root.left), unmake_tree(root.right))

    root = make_tree(ast.literal_eval(input()))

    val = int(input().strip())

    result_tree = insert_node(root, val)

    result = unmake_tree(result_tree)

    fptr.write(str(result) + '\n')

    fptr.close()
