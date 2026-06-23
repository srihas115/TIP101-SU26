# Problem 1: Is Odd-valued

Given the `root` of a binary tree, return the number of nodes that have odd values.


Evaluate the time complexity of your solution.


```python
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def count_odds(root):
	pass
```

Example Usage:


```python
Example Input Tree #1:

      2
     / \
    /   \
   3     5
  / \     \
 6   7     12

Input: root = 2
Expected Output: 3

Example Input Tree #2:

      2
     / \
    /   \
   4     2
  / \     \
 1   6     8

Input: root = 2
Expected Output: 1
```


<details>
  <summary>✨ <b>AI Hint: Binary Trees</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This problem requires you to understand binary trees. For a refresher on this topic, check out the Binary Trees section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/8#!cheatsheet).


If you need more help, try asking an AI tool like ChatGPT or GitHub Copilot to explain the concept of binary trees using a real-world analogy, and any following questions you have.


Once you grasp the idea, you can ask it to show you examples of binary trees in Python.
</details>
