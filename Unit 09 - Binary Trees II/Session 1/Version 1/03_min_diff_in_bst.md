# Problem 3: Minimum Difference in BST

Given the `root` of a binary search tree, return the minimum difference between the values of any two different nodes in the tree.


Evaluate the time complexity of your function.


```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_diff_in_bst(root):
	pass
```

Example Usage:


```python
Example Input Tree #1:

    4
   / \
  2   6
 / \
1   3

Example Input: root = 4
Expected Output: 1
Explanation: The smallest difference between any two nodes is 1 (2 - 1 = 1, 3 - 2 = 1)

Example Input Tree  #2:

   1
  / \
 0  48
    / \
   12 49

Example Input: root = 1
Expected Output: 1
Explanation: The smallest difference between any two nodes is 1 (1 - 0 = 1)
```


<details>
  <summary>✨ <b>AI Hint: Representing Infinite Values</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


To solve this problem, it may be helpful to know how to represent **positive or negative infinity** in Python. TO learn more, take a look at the Infinity section of the [Unit 9 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/9#!cheatsheet).


If you still have questions, try asking an AI tool like ChatGPT or GitHub Copilot to explain more about positive and negative infinity. For example, you might ask:


*"What is a common use case for positive or negative infinity in a program?"*
</details>
