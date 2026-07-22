class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_tail(head):
    pass

# linked list: num1 -> num2 -> num3
num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
delete_tail(num1)

# linked list: num1 -> num2

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

print(_to_list(num1))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - two-node list (tail removed, one node left)")
tn2 = Node(20)
tn1 = Node(10, tn2)
delete_tail(tn1)
print("  expected:", [10], "| got:", _to_list(tn1))

print("Test 2 - longer list (four nodes)")
q4 = Node(4)
q3 = Node(3, q4)
q2 = Node(2, q3)
q1 = Node(1, q2)
delete_tail(q1)
print("  expected:", [1, 2, 3], "| got:", _to_list(q1))


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

grade(delete_tail)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], expected=[1, 2])   # checks the updated first argument against this example
