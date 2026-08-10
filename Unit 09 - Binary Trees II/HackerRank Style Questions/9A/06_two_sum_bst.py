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
    pass

if __name__ == '__main__':
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    print("find_target(root, 9) ->", find_target(root, 9))
    print("find_target(root, 28) ->", find_target(root, 28))
