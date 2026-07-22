'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 2  ·  Version 1
  Problem 4: Convert Binary Linked List to Integer

  You are given the head of a linked list. Each value in the linked list is
  either 0 or 1, and the entire linked list represents a binary number.
  Return an integer that is the decimal value of the number represented by
  the linked list. The most significant bit is at the head of the linked
  list.

  Write your solution for `binary_to_int` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `binary_to_int` and its parameters exactly as given —
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

def binary_to_int(head):
    pass

# 1 -> 0 -> 1
num3 = Node(1)
num2 = Node(0, num3)
num1 = Node(1, num2)   # head of the list

int_num = binary_to_int(num1)
# 101 in binary is 5
print(int_num)  # Output: 5

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list, value 1")
single_one = Node(1)
print("  expected:", 1, "| got:", binary_to_int(single_one))

print("Test 2 - single-node list, value 0")
single_zero = Node(0)
print("  expected:", 0, "| got:", binary_to_int(single_zero))

print("Test 3 - longer binary number (1101 = 13)")
b4 = Node(1)
b3 = Node(0, b4)
b2 = Node(1, b3)
b1 = Node(1, b2)
print("  expected:", 13, "| got:", binary_to_int(b1))


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

grade(binary_to_int)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 0, 1], expected=5)   # checks the value your code returns against this example
