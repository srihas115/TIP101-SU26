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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Helper function to convert str to linked list
    def str_to_unique_ll(vals_str):
        if vals_str == "None":
            return None
        vals = [x.strip() for x in vals_str.split("->")]
        temp_head, nodes_dict = Node("temp"), {}
        temp_curr = temp_head
        for val in vals:
            if val not in nodes_dict:
                nodes_dict[val] = Node(val)
            temp_curr.next = nodes_dict[val]
            temp_curr = temp_curr.next
        return temp_head.next #Don't keep the temp head

    # Helper function to convert linked list to str
    def unique_ll_to_str(head):
        vals, curr, cycle = [], head, False
        while curr and not cycle:
            if curr.val in vals:
                cycle = True
            vals.append(curr.val)
            curr = curr.next
        if len(vals) == 0:
            return "None"
        return "->".join(vals)

    head = str_to_unique_ll(input())

    answer = has_cycle(head)
    list_str = unique_ll_to_str(head)
    result = str(answer) + "\n" + list_str

    fptr.write(result + '\n')

    fptr.close()
