'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 2  ·  Version 2
  Problem 1: Convert to Circular Linked List

  A circular linked list is a linked list where the tail node points at the
  head node. Write a function that transforms a singly linked list into a
  circular linked list. Return the head of the linked list. Evaluate the
  time and space complexity of your solution. Define your variables and
  provide a rationale for why you believe your solution has the stated time
  and space complexity.

  Write your solution for `make_circular` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `make_circular` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


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
