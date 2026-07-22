'''
==============================================================================
    Unit 6: Linked Lists II  ·  Session 1  ·  Version 2
    Problem 6: Was That a Crit?

    Given the `head` of a singly linked list, return the number of critical
    points. A critical point is a local minima or maxima. - The head and tail
    nodes are not considered critical points. - A node is a local minima if
    both the next and previous elements are greater than the current element -
    A node is a local maxima if both the next and previous elements are less
    than the current element.

    Evaluate the time and space complexity of your solution. Define your
    variables and provide a rationale for why you believe your solution has
    the stated time and space complexity.

    Write your solution for `count_critical_points` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `count_critical_points` and its parameters exactly as given —
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

def count_critical_points(head):
    pass

# Input List: 1 -> 2 -> 3 -> 3 -> 3 -> 5 -> 1 -> 3
_v = [1, 2, 3, 3, 3, 5, 1, 3]
_nodes = [Node(x) for x in _v]
for _i in range(len(_nodes) - 1):
    _nodes[_i].next = _nodes[_i + 1]
print(count_critical_points(_nodes[0]))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list (no critical points possible)")
single = Node(5)
print("  expected:", 0, "| got:", count_critical_points(single))

print("Test 2 - two-node list (no critical points possible)")
tw2 = Node(2)
tw1 = Node(1, tw2)
print("  expected:", 0, "| got:", count_critical_points(tw1))

print("Test 3 - all elements the same (no strict minima/maxima)")
same3 = Node(4)
same2 = Node(4, same3)
same1 = Node(4, same2)
print("  expected:", 0, "| got:", count_critical_points(same1))


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

grade(count_critical_points)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 3, 3, 5, 1, 3], expected=2)   # checks the value your code returns against this example
