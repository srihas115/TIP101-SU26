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
# Complete the 'find_target' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. TreeNode root
#  2. INTEGER k
#

def find_target(root, k):
    # Write your code
    seen = set()

    def dfs(node):
        if not node:
            return False
        if (k - node.val) in seen:
            return True
        seen.add(node.val)
        return dfs(node.left) or dfs(node.right)

    return dfs(root)


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

    target = int(input().strip())

    result = find_target(root, target)

    fptr.write(str(result) + '\n')

    fptr.close()
