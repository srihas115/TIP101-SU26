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
    a_len = 0
    curr_a = head_a
    while curr_a:
        a_len += 1
        curr_a = curr_a.next

    b_len = 0
    curr_b = head_b
    while curr_b:
        b_len += 1
        curr_b = curr_b.next

    curr_a = head_a
    curr_b = head_b

    if b_len > a_len:
        for i in range(b_len - a_len):
            curr_b = curr_b.next
    else:
        for i in range(a_len - b_len):
            curr_a = curr_a.next

    while curr_a is not curr_b:
        curr_a = curr_a.next
        curr_b = curr_b.next

    return curr_a

if __name__ == '__main__':
    shared = Node('c', Node('d'))
    head_a = Node('a', Node('b', shared))
    head_b = Node('x', shared)
    intersection = find_intersection(head_a, head_b)
    print("find_intersection(a->b->c->d, x->c->d) ->", intersection.value if intersection else None)
