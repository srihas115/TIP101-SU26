# Problem 3: Merge Two Sorted Linked Lists

Given the heads of two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the input lists. Return the head of the result list.


Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def merge_two_lists(head_a, head_b):
	pass
```

Example Usage:


```python
"""
Input: List 1: 1 -> 2 -> 4, List 2: 2 -> 3 -> 4
Input: head_a = 1, head_b = 2
Output: 1 -> 2 -> 2 -> 3 -> 4 -> 4
"""
```


### 💡 Hint: Temporary Head Technique


This problem may benefit from the temporary head technique. For reference, check out the [Unit 6 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/6#!cheatsheet).
