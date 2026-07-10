class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

'''


'''

# Time-Complexity: O(n)
# Space-Complexity: O(n)
def is_circular(head):
    seen = set()

    while head:
        if head not in seen:
            seen.add(head)
            head = head.next
        else:
            return True
    
    return False

# num1 -> num2 -> num3 -> num1
num1 = Node(1)
num2 = Node(2)
num3 = Node(3, num1)
num1.next = num2
num2.next = num3
print(is_circular(num1))

var1 = Node(1)
var2 = Node(2)
var3 = Node(3)
var1.next = var2
var2.next = var3
# var1 -> var2 -> var3
print(is_circular(var1))
