class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_last_node_in_cycle(head):
    seen = set()
    curr = head
    prev = None
    
    # iterate through the list
    while curr and curr not in seen:
        seen.add(curr)
        prev = curr
        curr = curr.next
        
    return prev


num4 = Node(4)
num3 = Node(3, num4)
num2 = Node(2, num3)
num1 = Node(1, num2)
num4.next = num1
print(find_last_node_in_cycle(num1).value) # type: ignore