class TreeNode():
      def __init__(self, key, value=None, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right

def inorder_successor(root, current):
      pass

# Build Example Tree #1/#2:
#           10
#          /  \
#         5    15
#        / \
#       1   8
#          / \
#         6   9

n1  = TreeNode(1)
n6  = TreeNode(6)
n9  = TreeNode(9)
n8  = TreeNode(8, left=n6, right=n9)
n5  = TreeNode(5, left=n1, right=n8)
n15 = TreeNode(15)
n10 = TreeNode(10, left=n5, right=n15)  # root

# Example 1: current = node with key 5 → successor is node with key 6
succ = inorder_successor(n10, n5)
# Expected: succ is a TreeNode; succ.key == 6

# Example 2: current = node with key 6 → successor is node with key 8
succ = inorder_successor(n10, n6)
# Expected: succ is a TreeNode; succ.key == 8
