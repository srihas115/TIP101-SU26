class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def ll_replace(head, original, replacement):
    if head is None: # linked list is empty
        return None
    if head.next is None: # linked list has only 1 element
        if head.value == original:
            head.value = replacement
    # edge cases ^^
    
    curr = head
    while curr is not None:
        if curr.value == original:
            curr.value = replacement
        curr = curr.next


def to_string(head): # to test your list
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"
print(to_string(head))