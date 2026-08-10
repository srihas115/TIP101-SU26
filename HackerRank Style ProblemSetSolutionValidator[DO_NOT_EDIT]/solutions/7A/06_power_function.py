#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'power' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER n
#

def power(x, n):
    # Write your code here
    if n == 0:
        return 1
    return x * power(x, n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = int(input().strip())

    n = int(input().strip())

    result = power(x, n)

    fptr.write(str(result) + '\n')

    fptr.close()
