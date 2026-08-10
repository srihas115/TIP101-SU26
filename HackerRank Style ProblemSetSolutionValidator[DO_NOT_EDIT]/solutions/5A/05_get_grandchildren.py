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
        grandchildren = []
        for child in self.children:
            grandchildren.extend(child.children)
        return grandchildren

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inp = input()

    if inp == '0':
        johndoe = Person("John", "Doe")
        janedoe = Person("Jane", "Doe")
        jimmydoe = Person("Jimmy", "Doe")
        johndoe.add_child(janedoe)
        janedoe.add_child(jimmydoe)
        assert johndoe.get_grandchildren() == [jimmydoe], "Test Case 0 Failed"
        result = "True"
    elif inp == '1':
        johndoe = Person("John", "Doe")
        janedoe = Person("Jane", "Doe")
        johndoe.add_child(janedoe)
        assert johndoe.get_grandchildren() == [], "Test Case 1 Failed"
        result = "True"
    elif inp == '2':
        splinter = Person("Master", "Splinter")
        leo = Person("Leonardo", "Turtle")
        raph = Person("Raphael", "Turtle")
        don = Person("Donatello", "Turtle")
        mich = Person("Michelangelo", "Turtle")
        shredder = Person("The", "Shredder")
        splinter.add_child(shredder)
        shredder.add_child(leo)
        shredder.add_child(raph)
        shredder.add_child(don)
        shredder.add_child(mich)
        assert splinter.get_grandchildren() == [leo, raph, don, mich], "Test Case 2 Failed"
        result = "True"
    elif inp == '3':
        johndoe = Person("John", "Doe")
        janedoe = Person("Jane", "Doe")
        jimmydoe = Person("Jimmy", "Doe")
        livydoe = Person("Livy", "Doe")
        babygronk = Person("Baby", "Gronk")
        johndoe.add_child(janedoe)
        janedoe.add_child(jimmydoe)
        janedoe.add_child(livydoe)
        livydoe.add_child(babygronk)
        assert johndoe.get_grandchildren() == [jimmydoe, livydoe], "Test Case 3 Failed"
        result = "True"
    elif inp == '4':
        johndoe = Person("John", "Doe")
        janedoe = Person("Jane", "Doe")
        jimmydoe = Person("Jimmy", "Doe")
        johndoe.add_child(janedoe)
        assert johndoe.get_grandchildren() == [], "Test Case 1 Failed"
        janedoe.add_child(jimmydoe)
        assert johndoe.get_grandchildren() == [jimmydoe], "Test Case 0 Failed"
        splinter = Person("Master", "Splinter")
        leo = Person("Leonardo", "Turtle")
        raph = Person("Raphael", "Turtle")
        don = Person("Donatello", "Turtle")
        mich = Person("Michelangelo", "Turtle")
        shredder = Person("The", "Shredder")
        splinter.add_child(shredder)
        shredder.add_child(leo)
        shredder.add_child(raph)
        shredder.add_child(don)
        shredder.add_child(mich)
        assert splinter.get_grandchildren() == [leo, raph, don, mich], "Test Case 2 Failed"
        livydoe = Person("Livy", "Doe")
        babygronk = Person("Baby", "Gronk")
        janedoe.add_child(livydoe)
        livydoe.add_child(babygronk)
        assert johndoe.get_grandchildren() == [jimmydoe, livydoe], "Test Case 3 Failed"
        littledoe = Person("Little", "Doe")
        jimmydoe.add_child(littledoe)
        assert janedoe.get_grandchildren() == [littledoe, babygronk], "Test Case 4 Failed"
        result = "True"
    else:
        # Ensure get_grandchildren() does not modify the people
        gen_1 = Person("John", "Doe")
        gen_2 = Person("Jane", "Doe")
        gen_1.add_child(gen_2)
        gen_3a = Person("Jimmy", "Doe")
        gen_3b = Person("Livy", "Doe")
        gen_2.add_child(gen_3a)
        gen_2.add_child(gen_3b)
        gen_4a = Person("Baby", "Gronk")
        gen_3a.add_child(gen_4a)
        gen_4b = Person("Little", "Doe")
        gen_3b.add_child(gen_4b)
        for person in [gen_1, gen_2, gen_3a, gen_3b, gen_4a, gen_4b]:
            person.get_grandchildren()
        # Ensure no one was modified
        assert gen_1.children == [gen_2], "Test Case 1 Failed"
        assert gen_2.children == [gen_3a, gen_3b], "Test Case 2 Failed"
        assert gen_3a.children == [gen_4a], "Test Case 3 Failed"
        assert gen_3b.children == [gen_4b], "Test Case 4 Failed"
        assert gen_4a.children == [], "Test Case 5 Failed"
        assert gen_4b.children == [], "Test Case 6 Failed"
        result = "True"

    fptr.write(result)
    fptr.close()
