# Problem 3: Delete Duplicates in a Linked List

Given the `head` of a sorted linked list, delete all elements that occur more than once in the list (*not just the duplicates*). The resulting list should maintain sorted order. Return the head of the linked list.


```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_dupes(head):
	pass
```

Example Input: `1 -> 2 -> 3 -> 3 -> 4 -> 5`


Example Output: `1 -> 2 -> 4 -> 5`


### 💡 Hint: Temporary Head Technique


This problem may benefit from the temporary head technique. For reference, check out the [Unit 6 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/6#!cheatsheet).
