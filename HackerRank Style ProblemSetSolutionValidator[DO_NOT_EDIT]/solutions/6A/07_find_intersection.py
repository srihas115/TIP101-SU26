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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Helper function to convert str -> linked list
    def str_to_linked_list_without_repetition(vals_str, nodes_dict={}):
        if vals_str == "None":
            return None, {}
        vals = [x.strip() for x in vals_str.split("->")]
        temp_head = Node("temp")
        temp_curr = temp_head
        for val in vals:
            if val in nodes_dict:
                temp_curr.next = nodes_dict[val]
            else:
                temp_curr.next = Node(val)
                nodes_dict[val] = temp_curr.next
            temp_curr = temp_curr.next
        return temp_head.next, nodes_dict #Don't keep the temp head

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
    head_a, dict_a = str_to_linked_list_without_repetition(input())
    head_b, _ = str_to_linked_list_without_repetition(input(), dict_a)

    # Call the function
    answer = find_intersection(head_a, head_b)
    if answer is not None:
        answer = answer.value

    # Turn the lists into a string
    list_str_a = linked_list_to_str(head_a)
    list_str_b = linked_list_to_str(head_b)

    # Bundle result in format <answer>\n<original linked list>
    result = str(answer) + "\n" + list_str_a + "\n" + list_str_b

    fptr.write(result)
    fptr.close()
