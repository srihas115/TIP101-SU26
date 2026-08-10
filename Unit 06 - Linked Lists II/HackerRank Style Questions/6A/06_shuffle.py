#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'shuffle' function below.
#
# The function is expected to return nothing.
# The function accepts HEAD head as parameter.
#

class Node:
   def __init__(self, value, next_node = None):
       self.value = value
       self.next = next_node

def shuffle(head):
    # Write your code here
    pass

if __name__ == '__main__':
    def linked_list_to_list(head):
        values = []
        while head:
            values.append(head.value)
            head = head.next
        return values

    head = Node('a', Node('b', Node('c', Node('d'))))
    shuffle(head)
    print("shuffle(a->b->c->d) ->", linked_list_to_list(head))
