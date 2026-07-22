class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_two_numbers(head_a, head_b):
    pass

# list 1: 2 -> 4 -> 3 (342)
# list 2: 5 -> 6 -> 4 (465)
# head_a = 2, head_b = 5
_a3 = Node(3)
_a2 = Node(4, _a3)
head_a = Node(2, _a2)

_b3 = Node(4)
_b2 = Node(6, _b3)
head_b = Node(5, _b2)

sum = add_two_numbers(head_a, head_b)

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

print(_to_list(sum))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-digit numbers with a carry (5 + 5 = 10)")
five_a = Node(5)
five_b = Node(5)
result1 = add_two_numbers(five_a, five_b)
print("  expected:", [0, 1], "| got:", _to_list(result1))

print("Test 2 - different-length numbers (9 + 91 = 100)")
nine = Node(9)
ninety_one_2 = Node(9)
ninety_one_1 = Node(1, ninety_one_2)
result2 = add_two_numbers(nine, ninety_one_1)
print("  expected:", [0, 0, 1], "| got:", _to_list(result2))


'''
==============================================================================
  PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import grade, test

grade(add_two_numbers)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([2, 4, 3], [5, 6, 4], expected=[7, 0, 8])   # checks the value your code returns against this example
