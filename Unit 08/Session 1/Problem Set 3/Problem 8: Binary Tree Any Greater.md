# Problem 8: Binary Tree Any Greater

Given a `value` and the `root` of a binary tree, write a function `contains_greater()` which returns `True` if any nodes greater than `value` exist in the tree. If no node greater than value exist, return `False`. Assume the tree is balanced.


Evaluate the time complexity of your solution.


```python
# Example Input Tree:
"""
      1
     / \
    /   \
   5     2
  / \
 4   3
"""
# Input: root = 1, value = 3
# Expected Output: True

# Example Input Tree:
"""
      1
     / \
    /   \
   5     2
  / \
 4   3
"""
# Input: root = 1, value = 10
# Expected Output: False

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def contains_greater(root, value):
	pass
```


### ✨ AI Hint: Balanced Trees


Tree problems will often specify whether or not you can assume a tree is balanced. This can affect the time complexity of your algorithm.


For a quick refresher, check out the Balanced Tree section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/8#!cheatsheet). If you need more help, try using an AI tool like ChatGPT or GitHub Copilot to show you examples of balanced trees and how they work. For example, you could ask:


*"You're an expert computer science tutor. Can you help me understand the concept of a balanced binary tree, using multiple examples and an analogy to real-world objects?"*
