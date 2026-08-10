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
    ll_len = 0
    curr = head
    while curr:
        ll_len += 1
        curr = curr.next

    if n <= 0 or n > ll_len: # handling edge cases for if a negative n or a n that is longer than the list itself
        return None

    target = ll_len - n
    curr = head
    for i in range(target):
        curr = curr.next
    return curr.value


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
    #inp = input()
    n = int(input())
    head = str_to_linked_list(input())

    # Call the function
    answer = find_nth_from_end(head, n)

    # Turn the list into a string
    list_str = linked_list_to_str(head)

    # Bundle result in format <answer>|<linked list>
    result = str(answer) + "\n" + list_str

    fptr.write(result)
    fptr.close()
