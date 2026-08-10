#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'find_val' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY names
#  2. STRING val
#

def find_val(names, val):
    # Write your code here
    low = 0
    high = len(names) - 1

    while low <= high:
        mid = (low + high) // 2

        if names[mid] == val:
            return mid
        elif names[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input list as a string and safely evaluate it to a Python list
    names = ast.literal_eval(input().strip())

    # Read the value to find, also stripping the surrounding quotes
    val = input().strip().strip("'")

    # Call the find_val function with names and val
    result = find_val(names, val)

    # Write the result to the file expected by HackerRank Style
    fptr.write(str(result) + '\n')

    fptr.close()
