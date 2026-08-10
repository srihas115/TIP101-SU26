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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    temp = input()

    if len(temp) > 45:
        input_string = temp
        chunks = input_string.split(", ")
        list_of_lists = [list(map(int, chunk.split())) for chunk in chunks]
        result = [find_max(lst) for lst in list_of_lists]
    else:
        result = find_max([int(n) for n in temp.split()])

    fptr.write(str(result) + '\n')

    fptr.close()
