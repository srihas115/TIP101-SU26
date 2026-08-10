#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'find_min_sublist_sum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER k
#

# Run-time complexity: O(n^2)
# Space-time complexity: O(1)
def find_min_sublist_sum2(nums, k):
    # Write your code here

    if (k > len(nums)):
        return 0

    subgroup_start = 0
    right = 0
    min_sum = float('inf')

    while subgroup_start + k <= len(nums):
        curr_sum = 0
        right = subgroup_start

        while right < subgroup_start + k:
            curr_sum += nums[right]
            right += 1

        if curr_sum < min_sum:
            min_sum = curr_sum

        subgroup_start += 1

    return min_sum

# Run-time complexity: O(n)
# Space-time complexity: O(1)
def find_min_sublist_sum(nums, k):
    if (k > len(nums)):
        return 0

    curr_sum = sum(nums[0:k]) # the first window of sliding window
    min_sum = curr_sum

    for i in range(k, len(nums)):
        curr_sum += nums[i]
        curr_sum -= nums[i - k]

        if curr_sum < min_sum:
            min_sum = curr_sum

    return min_sum

if __name__ == '__main__':
    print("find_min_sublist_sum([3, -2, 5, -1], 2) ->", find_min_sublist_sum([3, -2, 5, -1], 2))
    print("find_min_sublist_sum([4, 2, 1, 7], 3) ->", find_min_sublist_sum([4, 2, 1, 7], 3))
