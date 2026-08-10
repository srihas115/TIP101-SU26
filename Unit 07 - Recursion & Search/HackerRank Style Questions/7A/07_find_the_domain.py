#!/bin/python3

import math
import os
import random
import re
import sys
import ast




#
# Complete the 'search' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def search(nums, target):
    # Write your code here
    n = len(nums)

    lo = 0
    hi = n - 1

    start = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            start = mid
            hi = mid - 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    if start == -1:
        return [-1, -1]

    lo = 0
    hi = n - 1

    end = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            end = mid
            lo = mid + 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return [start, end]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = ast.literal_eval(input().strip())
    target = int(input().strip())

    result = search(nums, target)

    # Change here: Convert the entire list to a string that looks like a list
    fptr.write(str(result) + '\n')

    fptr.close()
