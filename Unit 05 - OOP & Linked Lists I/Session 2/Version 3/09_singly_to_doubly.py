'''
==============================================================================
    Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 3
    Problem 9: Singly to Doubly
    Write your solution in the space provided below, then click ▶ Run to validate it.
    (Full instructions and examples are in the problem set.)

    ⚠️  Keep every class, method, and function name exactly as the problem gives it,
        and use the exact variable names it asks for — the problem set solution validator looks those up
        by name (they're case-sensitive). If it can't find one, the results will tell
        you which name is missing.
==============================================================================
'''


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

crazy_in_love = Node("Crazy in Love")
formation = Node("Formation")
texas_hold_em = Node("Texas Hold 'Em")
crazy_in_love.next = formation
formation.next = texas_hold_em


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
