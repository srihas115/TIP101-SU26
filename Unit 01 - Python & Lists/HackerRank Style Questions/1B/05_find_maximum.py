#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'find_max' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY lst as parameter.
#

def find_max(lst):
    # Write your code here
    max = lst[0]
    for num in lst:
        if num > max:
            max = num
    return max

if __name__ == '__main__':
    print("find_max([1, 5, 3]) ->", find_max([1, 5, 3]))
    print("find_max([-10, -3, -7]) ->", find_max([-10, -3, -7]))
