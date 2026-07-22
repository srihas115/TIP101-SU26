'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 2
  Problem 4: Linked List Length

  Write a function `ll_length()` that takes in a `head` of a linked list as
  a parameter and returns the length of the linked list.

  Write your solution for `ll_length` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `ll_length` and its parameters exactly as given —
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

def ll_length(head):
    pass

# Linked List: num1 -> num2 -> num3
num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
head = num1
print(ll_length(head))

# Empty Linked List
head = None
print(ll_length(head))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list")
single = Node(9)
print("  expected:", 1, "| got:", ll_length(single))

print("Test 2 - longer list")
n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
print("  expected:", 5, "| got:", ll_length(n1))


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

grade(ll_length)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], expected=3)   # checks the value your code returns against this example
