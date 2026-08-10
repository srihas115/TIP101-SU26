#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'find_product' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY lst as parameter.
#

def find_product(lst):
    # Write your code here
    product = 1
    for num in lst:
        product *= num
    return product

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    temp = input()

    if len(temp) > 55:
        input_string = temp
        chunks = input_string.split(", ")
        list_of_lists = [list(map(int, chunk.split())) for chunk in chunks]
        result = [find_product(lst) for lst in list_of_lists]
    else:
        result = find_product([int(n) for n in temp.split()])

    fptr.write(str(result) + '\n')

    fptr.close()
