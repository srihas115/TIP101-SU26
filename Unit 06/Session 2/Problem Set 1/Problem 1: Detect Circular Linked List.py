class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
    pass

# num1 -> num2 -> num3 -> num1
print(is_circular(num1))

# var1 -> var2 -> var3
print(is_circular(var1))
