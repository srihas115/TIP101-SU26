# Problem 5: Are We There Yet?

Given the head of a linked list, return the length of its cycle.

A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.


Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


```python
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def cycle_length(head):
	pass
```

Example Usage:


```python
# Input List
# 1 -> 2 -> 3 -> 4
#      ^         |
#      |_________|
# Input: head = 1
```

Example Output:


```python
# Output: 3
```


### ✨ AI Hint: Multiple Pass Technique


*Key Skill: Use AI to explain code concepts*


This problem may require multiple traversals of the list. For reference, check out the [Unit 6 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/6#!cheatsheet).


For more help, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of the multiple pass technique.
