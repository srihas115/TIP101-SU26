# Two Sum BST

Source: HackerRank Style Unit 9 Assessment, Version A

## Question

Given the root of a binary search tree where each node has integer values and an integer k, return True
if there exist two nodes in the BST such that the sum of their values is equal to k, and False otherwise.
Hints:
- Maintain a list or set of seen node values. A set would be more performant for this use case.
- Traverse the tree using any method, depth first or breadth first. As you traverse, see if you can make the
sum using the current node and the list or set of seen node values

Example Input Tree #1:
      5
     / \
    /   \
   3     6
  / \     \
 2   4     7
Example Input: root = 5, k = 9
Expected Output: True
Explanation: There are three pairs of nodes that sum to k: 3 + 6 = 9, 5 + 4 = 9, 2 + 7 = 9
Example Input Tree #2:
      5
     / \
    /   \
   3     6
  / \     \
 2   4     7
Example Input: root = 5, k = 28
Expected Output: True
Explanation: There is no pair of nodes that sums to k
