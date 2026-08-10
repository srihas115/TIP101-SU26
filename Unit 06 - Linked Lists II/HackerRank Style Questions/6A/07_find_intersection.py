#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'find_intersection' function below.
#
# The function is expected to return a NODE.
# The function accepts following parameters:
#  1. HEAD head_a
#  2. HEAD head_b
#

class Node:
   def __init__(self, value, next_node = None):
       self.value = value
       self.next = next_node

def find_intersection(head_a, head_b):
    # Write your code here
    pass

if __name__ == '__main__':
    shared = Node('c', Node('d'))
    head_a = Node('a', Node('b', shared))
    head_b = Node('x', shared)
    intersection = find_intersection(head_a, head_b)
    print("find_intersection(a->b->c->d, x->c->d) ->", intersection.value if intersection else None)
