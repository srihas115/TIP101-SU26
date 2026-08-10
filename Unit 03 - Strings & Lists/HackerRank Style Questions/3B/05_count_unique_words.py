#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'count_unique_words' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING str as parameter.
#

def count_unique_words(str):
    # Write your code here
    lst = str.lower().split()
    return len(set(lst))

if __name__ == '__main__':
    print("count_unique_words('the cat and the dog') ->", count_unique_words('the cat and the dog'))
    print("count_unique_words('one one one') ->", count_unique_words('one one one'))
