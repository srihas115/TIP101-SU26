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
    pass

if __name__ == '__main__':
    perfect = TreeNode(1, TreeNode(2), TreeNode(3))
    not_perfect = TreeNode(1, TreeNode(2), None)
    print("is_perfect(perfect) ->", is_perfect(perfect))
    print("is_perfect(not_perfect) ->", is_perfect(not_perfect))
