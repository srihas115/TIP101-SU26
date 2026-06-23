"""Problem 3: Delete N Nodes after M Nodes

Solution intentionally left blank for practice.
"""

class Node:
    pass

    def __init__(self, val=0, next=None):
        pass

def delete_nodes(head, m, n):
    pass

# Example usage / test cases from the prompt:
# Input List #1:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13
# Input: head = 1, m = 2, n = 3
# Expected Output: 1
# Expected Output List: 1 -> 2 -> 6 -> 7 -> 11 -> 12
# Explanation: Keep the first (m = 2) nodes starting from the head of the linked List
# (1 ->2) show in black nodes.
# Delete the next (n = 3) nodes (3 -> 4 -> 5) show in read nodes.
# Continue with the same procedure until reaching the tail of the Linked List.
# Head of the linked list after removing nodes is returned.
# Input List #2:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11
# Input: head = 1, m = 1, n = 3
# Expected Output: 1
# Expected Output List: 1 -> 5 -> 9
