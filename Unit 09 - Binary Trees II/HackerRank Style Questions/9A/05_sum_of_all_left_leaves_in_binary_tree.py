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
    pass

if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("sum_left_leaves(root) ->", sum_left_leaves(root))
    print("sum_left_leaves(None) ->", sum_left_leaves(None))
