# Problem 6: Reverse Them, K?

Given the head of a singly linked list and an integer k, reverse the first k elements of the linked list. Return the new head of the linked list. If k is larger than the length of the list, reverse the entire list.


Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


```python
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse_first_k(head, k):
	pass
```

Example Usage:


```python
# Input List: 1 —> 2 —> 3 —> 4 —> 5
# Input: head = 1, k = 3
```

Example Output:


```python
# 3 -> 2 -> 1 -> 4 -> 5
```


<details>
  <summary>✨ <b>AI Hint: Multiple Pass Technique</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This problem may require multiple traversals of the list. For reference, check out the [Unit 6 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/6#!cheatsheet).


For more help, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of the multiple pass technique.
</details>
