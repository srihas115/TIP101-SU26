class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_cycle_nodes(head):
    pass

# num1 -> num2 -> num3 -> num4 -> num2
lst = collect_cycle_nodes(num1)
print(lst)

# var1 -> var2 -> var3 -> var4
lst2 = collect_cycle_nodes(var1)
print(lst2)
