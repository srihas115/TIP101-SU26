#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'find_nth_from_end' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. HEAD head
#  2. INTEGER n
#

class Node:
   def __init__(self, value, next_node = None):
       self.value = value
       self.next = next_node

def find_nth_from_end(head, n):
    # Write your code here
    pass

if __name__ == '__main__':
    head = Node('a', Node('b', Node('c', Node('d'))))
    print("find_nth_from_end(a->b->c->d, 2) ->", find_nth_from_end(head, 2))
    print("find_nth_from_end(a->b->c->d, 5) ->", find_nth_from_end(head, 5))
