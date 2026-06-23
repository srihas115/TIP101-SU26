# Problem 4: Convert Binary Number in a Linked List to Integer

You are given the head of a linked list. Each value in the linked list is either 0 or 1, and the entire linked list represents a binary number. Return an integer that is the decimal value of the number represented by the linked list. The most significant bit is at the head of the linked list.


```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def binary_to_int(head):
	pass
```

Example Usage:


```python
# 1 -> 0 -> 1
num3 = Node(1)
num2 = Node(0, num3)
num1 = Node(1, num2)   # head of the list

int_num = binary_to_int(num1)
# 101 in binary is 5
print(int_num)  # Output: 5
```

Example Output: `5`


### ✨ AI Hint: Binary to Decimal


*Key Skill: Use AI to explain code concepts*


This problem requires you to know how to convert a binary (base 2) number to a decimal (base 10) number. If you are unfamiliar with how to do this, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of how to convert binary to decimal.
