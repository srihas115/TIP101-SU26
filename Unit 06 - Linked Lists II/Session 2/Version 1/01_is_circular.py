class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

'''


'''

# Time-Complexity: O(n)
# Space-Complexity: O(n)
def is_circular(head):
    seen = set()

    while head:
        if head not in seen:
            seen.add(head)
            head = head.next
        else:
            return True
    
    return False

# num1 -> num2 -> num3 -> num1
num1 = Node(1)
num2 = Node(2)
num3 = Node(3, num1)
num1.next = num2
num2.next = num3
print(is_circular(num1))

var1 = Node(1)
var2 = Node(2)
var3 = Node(3)
var1.next = var2
var2.next = var3
# var1 -> var2 -> var3
print(is_circular(var1))


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

grade(is_circular)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([[1, 2, 3], 0], expected=True)   # checks the value your code returns against this example
