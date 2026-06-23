# Problem 6: Post-order Traversal

Given the `root` of a binary tree, return a list representing the postorder traversal of its nodes' values. In an postorder traversal we traverse the left subtree, then the right subtree, then the current node.


Evaluate the time complexity of your function.


```python
# Example Input Tree:
"""For example:
      1
     / \
    /   \
   2     3
  / \     \
 4   5     6
"""
# Input: root = 1
# Expected Output: [4, 5, 2, 6, 3, 1]

# Input: root = None
# Output: []

# Example Input Tree
""" 1 """
# Input: root = 1
# Output: [1]

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def postorder_traversal(root):
	pass
```


### ✨ AI Hint: Traversing Trees


*Key Skill: Use AI to explain code concepts*


This problem requires you to traverse a binary tree. For a refresher on this topic, check out the Tree Traversal section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/8#!cheatsheet).


Still have questions? Try asking an AI tool like ChatGPT or GitHub Copilot to explain the different types of binary tree traversal. You can use the following prompt as a starting point:


*"You're an expert computer science tutor. Please explain the different types of binary tree traversal, and show me how they would each work on an example tree."*


Hint: Be sure to learn about "preorder", "postorder", and "inorder" traversals!
