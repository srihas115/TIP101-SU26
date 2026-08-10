#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'Person' class below.
#
# The method 'get_grandchildren' is expected to return a LIST of the person's grandchildren.
#

class Person:
    def __init__(self, first, last):
        self.last_name = last
        self.first_name = first
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    # Write your code here
    def get_grandchildren(self):
        pass

if __name__ == '__main__':
    john = Person("John", "Doe")
    jane = Person("Jane", "Doe")
    jimmy = Person("Jimmy", "Doe")
    john.add_child(jane)
    jane.add_child(jimmy)
    print("john.get_grandchildren() ->", john.get_grandchildren())
    print("[person.first_name for person in john.get_grandchildren()] ->", [person.first_name for person in john.get_grandchildren()])
