#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'get_patients' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING doctor
#  2. DICTIONARY patients
#

def get_patients(doctor, patients):
    # Write your code here
    pass

if __name__ == '__main__':
    patients = {"Jane Doe": "Dr. Grey", "Alex Kim": "Dr. Grey", "Sam Lee": "Dr. House"}
    print("get_patients('Dr. Grey', patients) ->", get_patients("Dr. Grey", patients))
    print("get_patients('Dr. House', patients) ->", get_patients("Dr. House", patients))
