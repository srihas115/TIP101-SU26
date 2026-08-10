#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'copy_first_n_nodes' function below.
#
# The function is expected to return a HEAD.
# The function accepts following parameters:
#  1. HEAD head
#  2. INTEGER n
#

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

def copy_first_n_nodes(head, n):
    # Write your code here
    if not head:
        return None

    beforeTrueHead = Node(None)
    copyCurr = beforeTrueHead
    curr = head
    counter = 0

    while curr is not None and counter < n:
        copyCurr.next = Node(curr.value)
        copyCurr = copyCurr.next
        curr = curr.next
        counter += 1

    return beforeTrueHead.next

if __name__ == '__main__':
    def linked_list_to_list(head):
        values = []
        while head:
            values.append(head.value)
            head = head.next
        return values

    head = Node('a', Node('b', Node('c', Node('d'))))
    copied = copy_first_n_nodes(head, 3)
    print("copy_first_n_nodes(a->b->c->d, 3) ->", linked_list_to_list(copied))
    print("copied head is original head ->", copied is head)
