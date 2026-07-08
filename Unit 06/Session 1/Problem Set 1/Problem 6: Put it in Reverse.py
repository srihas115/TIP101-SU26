class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse(head):
    if head is None:
        return None
    if head.next is None:
        return head
    
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next   # temporarily store the next node
        curr.next = prev        # reverse the current node's pointer
        prev = curr             # move the prev pointer forward
        curr = next_node        # move the curr pointer forward
    return prev                 # prev becomes the new head of the reversed list

# Taken from Problem 3: Remove Tail.py
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# Input List: 1 -> 2 -> 3 -> 4
# Input: head = 1
head = Node(1, Node(2, Node(3, Node(4))))
reversed_head = reverse(head)
print_list(reversed_head)
