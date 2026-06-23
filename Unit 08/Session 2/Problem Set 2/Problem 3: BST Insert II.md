# Problem 3: BST Insert II

Given the `root` of a binary search tree, insert a new node with a given `value` into the tree. Return the `root` of the modified tree. If a node with the given value already exists, place the new node in the right subtree. You do not need to maintain a balanced tree.


Evaluate the time complexity of your function.


```python
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def insert_with_duplicates(root, value):
	pass
```

Example Usage:


```python
Example Input Tree #1:

      10
     /  \
    /    \
   8      15
  / \
 1   6

Input: root = 10, value = 9
Expected Output: root = 10
Expected Output Tree:

      10
     /  \
    /    \
   8      15
  / \
 1   6
      \
       9


Example Input Tree #2:

      10
     /  \
    /    \
   8      15
  / \
 1   6

Input: root = 10, value = 8
Expected Output: root = 10
Expected Output Tree:

      10
     /  \
    /    \
   8      15
  / \
 1   6
      \
       8


Example Input Tree #3: Empty Tree (None)

Input: root = None, value = 4
Expected Output: root = 4
Expected Output Tree:

      4
```


### ✨ AI Hint: Binary Search Trees


*Key Skill: Use AI to explain code concepts*


This problem requires you to be familiar with binary search trees (BSTs). This data structure is incredibly useful, and is often used in many coding interviews.


For a refresher on this topic, check out the Binary Search Tree section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/8#!cheatsheet).


To go deeper, you can ask an AI tool like ChatGPT or GitHub Copilot to explain the concept of binary search trees, how they work, and how to implement them in Python. You can also visit the [VisuAlgo BST Visualizer](https://visualgo.net/en/bst) to see how binary search trees work visually.
