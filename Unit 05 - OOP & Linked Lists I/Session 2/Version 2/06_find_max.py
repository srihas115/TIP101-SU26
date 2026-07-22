class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_max(head):
    pass

num4 = Node(10)
num3 = Node(30, num4)
num2 = Node(15, num3)
num1 = Node(20, num2)

# linked list: num1 -> num2 -> num3 -> num4
max_val = find_max(num1)
print(max_val)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node(42)
print("  expected:", 42, "| got:", find_max(single))

print("Test 2 - all negative numbers")
neg3 = Node(-1)
neg2 = Node(-5, neg3)
neg1 = Node(-10, neg2)
print("  expected:", -1, "| got:", find_max(neg1))

print("Test 3 - duplicate max values")
dup3 = Node(7)
dup2 = Node(7, dup3)
dup1 = Node(3, dup2)
print("  expected:", 7, "| got:", find_max(dup1))


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

grade(find_max)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([20, 15, 30, 10], expected=30)   # checks the value your code returns against this example
