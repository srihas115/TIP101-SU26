#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'peak_element' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LIST of INTEGERS nums as parameter.
#

def peak_element(nums):
    # Write your code here
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low

if __name__ == '__main__':
    print("peak_element([1, 2, 3, 1]) ->", peak_element([1, 2, 3, 1]))
    print("peak_element([1, 2, 1, 3, 5, 6, 4]) ->", peak_element([1, 2, 1, 3, 5, 6, 4]))
