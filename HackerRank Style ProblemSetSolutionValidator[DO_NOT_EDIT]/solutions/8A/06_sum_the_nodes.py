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
# Complete the 'sum_tree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts TreeNode root as parameter.
#

def sum_tree(root):
    # Write your code here
    if not root:
        return 0

    return root.val + sum_tree(root.left) + sum_tree(root.right)

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

    root = make_tree(ast.literal_eval(input()))

    result = sum_tree(root)

    fptr.write(str(result) + '\n')

    fptr.close()
