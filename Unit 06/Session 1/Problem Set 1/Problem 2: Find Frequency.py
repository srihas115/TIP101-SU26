class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1

# Time Complexity: O(n)
# Space Complexity: O(1)
def count_element(head, val):
    curr = head
    counter = 0
    
    while curr is not None:
        if curr.value == val:
            counter += 1
        curr = curr.next
    
    print(counter)

# Test
head = Node(3, Node(1, Node(2, Node(1))))
count_element(head, 1)