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
    for value in values:
        tail.next = Node(value)
        tail = tail.next

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    instring = input()

    if len(instring) > 50:
        def parse_input(input_string):
            # Split the input string at commas to create major segments
            major_segments = input_string.split(',')
            # Trim spaces and organize into a clean list
            cleaned_segments = [segment.strip() for segment in major_segments]
            return cleaned_segments
        parsed = parse_input(instring)

        def linked_list_to_string(head):
            values = []
            current = head
            while current:
                values.append(current.value)
                current = current.next
            return " ".join(values)

        def parse_and_extend_list(input_string):
            # Split the input string into initial elements and values to add
            parts = input_string.split(';')
            initial_elements = parts[0].strip().split()
            new_values = parts[1].strip().split()

            # Create the initial linked list from the first part
            if initial_elements:
                head = Node(initial_elements[0])
                current = head
                for element in initial_elements[1:]:
                    current.next = Node(element)
                    current = current.next
            tail = current  # The last node is the tail

            # Extend the linked list with new values
            extend_linked_list(tail, new_values)

            # Return the complete linked list as a string
            return linked_list_to_string(head)

        result = ""

        for part in parsed:
            result += parse_and_extend_list(part)
    else:
        def linked_list_to_string(head):
            values = []
            current = head
            while current:
                values.append(current.value)
                current = current.next
            return " ".join(values)

        def parse_and_extend_list(input_string):
            # Split the input string into initial elements and values to add
            parts = input_string.split(';')
            initial_elements = parts[0].strip().split()
            new_values = parts[1].strip().split()

            # Create the initial linked list from the first part
            if initial_elements:
                head = Node(initial_elements[0])
                current = head
                for element in initial_elements[1:]:
                    current.next = Node(element)
                    current = current.next
            tail = current  # The last node is the tail

            # Extend the linked list with new values
            extend_linked_list(tail, new_values)

            # Return the complete linked list as a string
            return linked_list_to_string(head)

        result = parse_and_extend_list(instring)

    fptr.write(result)

    fptr.close()
