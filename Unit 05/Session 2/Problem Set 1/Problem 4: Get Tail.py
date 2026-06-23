class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def get_tail(head):
    pass

# Build: num1 -> num2 -> num3
num1 = Node("num1")
num2 = Node("num2")
num3 = Node("num3")
num1.next = num2
num2.next = num3

head = num1
tail = get_tail(head)   # or get_tail(num1)
print(tail)             # expected: num3
