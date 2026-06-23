# Problem 1: Is Even-valued

Given the `root` of a binary tree, return `True` if every node in the tree has an even value and `False` otherwise.


```python
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def is_even(root):
	pass
```

Example Usage:


```python
Example Input Tree #1

      2
     / \
    /   \
   4     10
  / \     \
 6   8     12

Input: root = 2
Expected Output: True

Example Input Tree #2

      2
     / \
    /   \
   4     2
  / \     \
 1   6     8

Input: root = 2
Expected Output: False
```


### ✨ AI Hint: Binary Trees


*Key Skill: Use AI to explain code concepts*


This problem requires you to understand binary trees. For a refresher on this topic, check out the Binary Trees section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/8#!cheatsheet).


If you need more help, try asking an AI tool like ChatGPT or GitHub Copilot to explain the concept of binary trees using a real-world analogy, and any following questions you have.


Once you grasp the idea, you can ask it to show you examples of binary trees in Python.
