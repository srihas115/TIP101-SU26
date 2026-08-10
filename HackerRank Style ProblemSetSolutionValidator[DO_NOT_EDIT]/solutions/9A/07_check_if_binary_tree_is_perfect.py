#!/bin/python3

import math
import os
import random
import re
import sys
import ast


# HINT: Using a deque might help
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#
# Complete the 'is_perfect' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts TreeNode root as parameter.
#

def is_perfect(root):
    # Write your code here
    if root is None:
        return True

    queue = deque([root])
    leaf_level = None
    level = 0

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()

            is_leaf = node.left is None and node.right is None

            if is_leaf:
                if leaf_level is None:
                    leaf_level = level
                elif level != leaf_level:
                    return False
            else:
                if node.left is None or node.right is None:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        level += 1

    return True

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

    result = is_perfect(root)

    fptr.write(str(result) + '\n')

    fptr.close()
