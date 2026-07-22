'''
==============================================================================
    Unit 6: Linked Lists II  ·  Session 1  ·  Version 3
    Problem 2: Frequency Map

    Given the head of a linked list, return a dictionary that maps each unique
    element in the list to its frequency.

    Evaluate the time and space complexity of your solution. Define your
    variables and provide a rationale for why you believe your solution has
    the stated time and space complexity.

    Write your solution for `frequency_map` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `frequency_map` and its parameters exactly as given —
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

def frequency_map(head):
    pass

# Input List: 1 -> 2 -> 3 -> 4 -> 2 -> 3
# Input: head = 1
_vals = [1, 2, 3, 4, 2, 3]
_nodes = [Node(x) for x in _vals]
for _i in range(len(_nodes) - 1):
    _nodes[_i].next = _nodes[_i + 1]
print(frequency_map(_nodes[0]))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (head is None)")
print("  expected:", {}, "| got:", frequency_map(None))

print("Test 2 - single-node list")
single = Node('x')
print("  expected:", {'x': 1}, "| got:", frequency_map(single))

print("Test 3 - list with duplicate values")
d2 = Node('y')
d1 = Node('y', d2)
print("  expected:", {'y': 2}, "| got:", frequency_map(d1))


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

grade(frequency_map)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4, 2, 3], expected={1: 1, 2: 2, 3: 2, 4: 1})   # checks the value your code returns against this example
