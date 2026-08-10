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
    if head is None: # edge case for empty linked list
        return None

    curr = head
    while curr and curr.next:
        temp = curr.value
        curr.value = curr.next.value
        curr.next.value = temp
        curr = curr.next.next



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

    # Read and convert test input
    head = str_to_linked_list(input())

    # Call the function
    answer = shuffle(head)

    # Turn the list back into a string
    list_str = linked_list_to_str(head)

    fptr.write(list_str)
    fptr.close()
