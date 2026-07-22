'''
==============================================================================
    Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 3
    Problem 9: Tom and Jerry / Chase List
    Write your solution in the space provided below, then click ▶ Run to validate it.
    (Full instructions and examples are in the problem set.)

    ⚠️  Keep every class, method, and function name exactly as the problem gives it,
        and use the exact variable names it asks for — the problem set solution validator looks those up
        by name (they're case-sensitive). If it can't find one, the results will tell
        you which name is missing.
==============================================================================
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# From Problem 9:
mouse = Node("Jerry")
cat = Node("Tom", mouse)

# Problem 10: add dog so the list is dog -> cat -> mouse
dog = Node("Spike", cat)

print(dog.value)
print(dog.next.value)
print(dog.next.next.value)
print(cat.value)
print(cat.next.value)
print(mouse.next)

# --- Merged from Problem 10: Chase List.py ---
print(dog.value)
print(dog.next is cat)
print(dog.next.value)
print(cat.next is mouse)
print(cat.next.value)
print(mouse.next)


'''
==============================================================================
    PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import check_setup

check_setup()   # ▶ Run this file to validate your work
