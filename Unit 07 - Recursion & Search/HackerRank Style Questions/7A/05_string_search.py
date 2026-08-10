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
    names = ['Ada', 'Grace', 'Katherine', 'Mae']
    print("find_val(names, 'Katherine') ->", find_val(names, 'Katherine'))
    print("find_val(names, 'Sally') ->", find_val(names, 'Sally'))
