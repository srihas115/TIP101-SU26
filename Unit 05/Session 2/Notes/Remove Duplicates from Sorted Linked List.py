'''
Write a function to remove all duplicate values from a sorted linked list. After removing duplicates, each element in the list should appear only once.
Examples:
Input: head = [1 -> 1 -> 2]Output: [1 -> 2]
Input: head = [1 -> 1 -> 2 -> 3 -> 3]Output: [1 -> 2 -> 3]
Input: head = []Output: []
'''

def remove_duplicates_from_sorted_ll(head):
    curr = head
    while (curr is not None) and (curr.next is not None):
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return head

class Node:
    def __init__(self, v, n=None) -> None:
        self.val = v
        self.next = n


def build_ll(values):
    head = None
    tail = None
    for val in values:
        node = Node(val)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
    return head


def ll_to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


print(ll_to_list(remove_duplicates_from_sorted_ll(build_ll([1, 1, 2]))))       # [1, 2]
print(ll_to_list(remove_duplicates_from_sorted_ll(build_ll([1, 1, 2, 3, 3])))) # [1, 2, 3]
print(ll_to_list(remove_duplicates_from_sorted_ll(build_ll([]))))              # []

