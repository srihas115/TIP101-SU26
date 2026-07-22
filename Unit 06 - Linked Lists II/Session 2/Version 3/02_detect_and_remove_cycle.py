'''
==============================================================================
    Unit 6: Linked Lists II  ·  Session 2  ·  Version 3
    Problem 2: Detect and Remove Cycle

    Given the head of a linked list, write a function that removes any cycles
    in the linked list. Return the head of the list.

    Evaluate the time and space complexity of your solution. Define your
    variables and provide a rationale for why you believe your solution has
    the stated time and space complexity.

    Write your solution for `detect_and_remove_cycle` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `detect_and_remove_cycle` and its parameters exactly as given —
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

def detect_and_remove_cycle(head):
    pass

def _to_list_bounded(head, limit=50):
    # Bounded traversal: if the cycle wasn't actually removed, this stops after
    # `limit` nodes instead of looping forever.
    vals = []
    seen = 0
    while head is not None and seen < limit:
        vals.append(head.value)
        head = head.next
        seen += 1
    still_going = head is not None
    return vals, still_going

# Input List: 1 -> 2 -> 3 -> 1 (circular)
c3 = Node(3)
c2 = Node(2, c3)
c1 = Node(1, c2)
c3.next = c1
result = detect_and_remove_cycle(c1)
vals, still_going = _to_list_bounded(result)
print("  expected: [1, 2, 3], cycle removed | got:", vals, ", still going past 50 nodes:", still_going)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node self-cycle")
self_node = Node(9)
self_node.next = self_node
result1 = detect_and_remove_cycle(self_node)
vals1, still_going1 = _to_list_bounded(result1)
print("  expected:", [9], "cycle removed | got:", vals1, ", still going:", still_going1)

print("Test 2 - list with no cycle (should be left unchanged)")
nc2 = Node(2)
nc1 = Node(1, nc2)
result2 = detect_and_remove_cycle(nc1)
vals2, still_going2 = _to_list_bounded(result2)
print("  expected:", [1, 2], "| got:", vals2, ", still going:", still_going2)


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

grade(detect_and_remove_cycle)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([[1, 2, 3], 0], expected=[1, 2, 3])   # checks the value your code returns against this example
