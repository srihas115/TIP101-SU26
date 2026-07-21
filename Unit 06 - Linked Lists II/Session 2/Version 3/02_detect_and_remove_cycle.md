# Problem 2: Detect and Remove Cycle in a Linked List

Given the head of a linked list, write a function that removes any cycles in the linked list. Return the head of the list.


Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def detect_and_remove_cycle(head):
	pass
```

Example Usage:


```python
"""
Input List
1 -> 2 -> 3
^         |
|_________|
Input: head = 1
Expected Return Value: 1
Expected Result List: 1 -> 2 -> 3

"""
```


<details>
  <summary>✨ <b>AI Hint: Multiple Pass Technique</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This problem may require multiple traversals of the list. For reference, check out the [Unit 6 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/6#!cheatsheet).


For more help, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of the multiple pass technique.
</details>
