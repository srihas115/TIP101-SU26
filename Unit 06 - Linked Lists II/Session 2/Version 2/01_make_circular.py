class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def make_circular(head):
    pass

# Input List: num1 -> num2 -> num3
num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
make_circular(num1)
print("  expected: True | got:", num3.next is num1)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.
# Note: checks use pointer identity (bounded) rather than traversal, since the
# result is circular and an unbounded traversal would infinite-loop.

print("Test 1 - single-node list (self-loop)")
single = Node(9)
make_circular(single)
print("  expected:", True, "| got:", single.next is single)

print("Test 2 - two-node list")
t2 = Node('B')
t1 = Node('A', t2)
make_circular(t1)
print("  expected:", True, "| got:", t2.next is t1)


'''
==============================================================================
  PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import grade

grade(make_circular)   # ▶ Run this file to validate your solution
