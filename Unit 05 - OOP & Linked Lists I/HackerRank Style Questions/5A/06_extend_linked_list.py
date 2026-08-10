#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'extend_linked_list' function below.
#
# The function is not expected to return anything.
# The function accepts following parameters:
#  1. STRING tail
#  2. LIST(STRING) values
#

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

def extend_linked_list(tail, values):
    # Write your code here
    pass

if __name__ == '__main__':
    def linked_list_to_list(head):
        values = []
        while head:
            values.append(head.value)
            head = head.next
        return values

    head = Node('a', Node('b', Node('c')))
    tail = head.next.next
    extend_linked_list(tail, ['d', 'e', 'f'])
    print("extended list ->", linked_list_to_list(head))
