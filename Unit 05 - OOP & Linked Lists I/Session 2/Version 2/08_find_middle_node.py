class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_middle_node(head):
    pass

# linked list: num1 -> num2 -> num3 -> num4
num4 = Node(4)
num3 = Node(3, num4)
num2 = Node(2, num3)
num1 = Node(1, num2)
head = num1
mid = find_middle_node(head)
# mid == num2
print(mid.value if mid else None)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node('only')
result1 = find_middle_node(single)
print("  expected:", 'only', "| got:", result1.value if result1 else None)

print("Test 2 - odd-length list (3 nodes)")
o3 = Node(3)
o2 = Node(2, o3)
o1 = Node(1, o2)
result2 = find_middle_node(o1)
print("  expected:", 2, "| got:", result2.value if result2 else None)

print("Test 3 - two-node list (first middle per the even-length rule)")
t2 = Node('B')
t1 = Node('A', t2)
result3 = find_middle_node(t1)
print("  expected:", 'A', "| got:", result3.value if result3 else None)


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

grade(find_middle_node)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4], expected=2)   # checks the value your code returns against this example
