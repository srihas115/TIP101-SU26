# Problem 6: In-order Traversal

Given the `root` of a binary tree, return a list representing the inorder traversal of its nodes' values. In an inorder traversal we traverse the left subtree, then the current node, then the right subtree.


```python
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def inorder_traversal(root):
	pass
```

Example Usage:


```python
Example Input Tree #1:
     1
      \
       2
      /
     3

Input: root = 1
Expected Output: [1,3,2]

Example Input Tree #2 :

Input: root = None
Output: []

Example Input Tree #3:
    1

Input: root = 1
Output: [1]
```


<details>
  <summary>✨ <b>AI Hint: Traversing Trees</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This problem requires you to traverse a binary tree. For a refresher on this topic, check out the Tree Traversal section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/8#!cheatsheet).


Still have questions? Try asking an AI tool like ChatGPT or GitHub Copilot to explain the different types of binary tree traversal. You can use the following prompt as a starting point:


*"You're an expert computer science tutor. Please explain the different types of binary tree traversal, and show me how they would each work on an example tree."*


Hint: Be sure to learn about "preorder", "postorder", and "inorder" traversals!
</details>
