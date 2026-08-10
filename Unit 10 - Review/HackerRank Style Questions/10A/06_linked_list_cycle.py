#!/bin/python3

import math
import os
import random
import re
import sys



class Node:
   def __init__(self, value, next=None):
       self.val = value
       self.next = next

#
# Complete the 'has_cycle' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts Node head as parameter.
#

def has_cycle(head):
    # Write your code here
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False

if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    a.next = b
    b.next = c
    c.next = b
    print("has_cycle(a->b->c->b) ->", has_cycle(a))

    x = Node('x', Node('y'))
    print("has_cycle(x->y) ->", has_cycle(x))
