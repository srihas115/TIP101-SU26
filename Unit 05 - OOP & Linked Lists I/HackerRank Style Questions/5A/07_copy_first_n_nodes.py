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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Helper function to convert str -> linked list
    def str_to_linked_list(vals_str):
        if vals_str == "None":
            return None
        vals = vals_str.split("->")
        temp_head = Node("temp")
        temp_curr = temp_head
        for val in vals:
            temp_curr.next = Node(val.strip())
            temp_curr = temp_curr.next
        return temp_head.next #Don't keep the temp head

    # Helper function to convert linked list to str
    def linked_list_to_str(head):
        list_str = ""
        curr = head
        while curr:
            list_str += curr.value
            if curr.next:
                list_str += "->"
            curr = curr.next
        if len(list_str) == 0:
            return "None"
        return list_str

    def verify_is_copy(orig_ll, new_ll):
        orig_curr = orig_ll
        new_curr = new_ll
        while orig_curr and new_curr:
            if orig_curr == new_curr: # Compare NODES, not values
                return False
            orig_curr = orig_curr.next
            new_curr = new_curr.next
        return True

    # Read and convert test input
    n = int(input())
    head = str_to_linked_list(input())

    # Call the function
    answer = copy_first_n_nodes(head, n)

    # Turn the list into a string
    list_str = linked_list_to_str(head)
    answer_str = linked_list_to_str(answer)

    # Bundle result in format <result linked list>\n<original linked list>
    result = answer_str + "\n" + list_str

    # Verify the copy
    is_copy = verify_is_copy(head, answer)
    if not is_copy:
        result += "\nNot a copy - the same nodes were found in both input and output"

    fptr.write(result)
    fptr.close()
