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
    pass

if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print("sum_tree(1, 2, 3) ->", sum_tree(root))
    print("sum_tree(None) ->", sum_tree(None))
