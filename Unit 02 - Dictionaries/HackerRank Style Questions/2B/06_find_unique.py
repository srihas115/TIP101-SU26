#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'find_unique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY nums as parameter.
#

def find_unique(nums):
    # Write your code here
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    for k, v in freq_dict.items():
        if v == 1:
            return k

    return None

if __name__ == '__main__':
    print("find_unique([1, 2, 2, 3, 3]) ->", find_unique([1, 2, 2, 3, 3]))
    print("find_unique([4, 4, 5]) ->", find_unique([4, 4, 5]))
