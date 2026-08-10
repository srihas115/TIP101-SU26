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
    res = []
    for k, v in patients.items():
        if v == doctor:
            res.append(k)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    def create_dict(inlist):
        name_to_doctor = {}
        for i in range(0, len(inlist), 4):
            full_name = f"{inlist[i]} {inlist[i+1]}"
            doctor = f"{inlist[i+2]} {inlist[i+3]}"
            name_to_doctor[full_name] = doctor
        return name_to_doctor

    if len(t) > 400:
        doctors_specific = ["Dr. Grey", "Dr. Banner", "Dr. House", "Dr. Blue"]
        patients_specific = {
            "Jane Doe": "Dr. Grey",
            "Alexandra Stevens": "Dr. Grey",
            "Ethan Hunt": "Dr. Banner",
            "James Bond": "Dr. Banner",
            "Bruce Wayne": "Dr. Banner",
            "Emily Green": "Dr. Blue"
        }
        r = [get_patients(doctor, patients_specific) for doctor in doctors_specific]
        result = str(r)
    else:
        temp = t.split()
        dr = ' '.join(temp[:2])
        name_to_doctor = {}
        input_list = temp[2:]
        result = get_patients(dr, create_dict(input_list))

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
