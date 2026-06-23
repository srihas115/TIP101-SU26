# Problem 4: Does it Cycle?

Given the head of a linked list, return `True` if the list has a cycle in it and `False` otherwise. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.


Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


```python
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def has_cycle(head):
	pass
```

Example Usage:


```python
# Input List:
# 1 -> 2 -> 3 -> 4
#      ^         |
#      |---------|
# Input: head = 1
```

Example Output:


```python
# True
```


### ✨ AI Hint: Slow and Fast Pointers


*Key Skill: Use AI to explain code concepts*


This problem requires a variation of the two-pointer technique called the slow and fast pointer technique! For reference, check out the [Unit 6 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/6#!cheatsheet).


For more help, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of the slow and fast pointer technique.
