#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'find_sum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY lst as parameter.
#

def find_sum(lst):
    # Write your code here
    sum = 0
    for num in lst:
        sum += num
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    temp = input()

    if len(temp) > 70:
        input_string = temp
        chunks = input_string.split(", ")
        list_of_lists = [list(map(int, chunk.split())) for chunk in chunks]
        result = [find_sum(lst) for lst in list_of_lists]
    else:
        result = find_sum([int(n) for n in temp.split()])

    fptr.write(str(result) + '\n')

    fptr.close()
