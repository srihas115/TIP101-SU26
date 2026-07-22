class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def inorder_traversal_1(root): # left, visit, right
    if root is None: # base case
        return []
    
    res = []
    
    res.extend(inorder_traversal_1(root.left))
    res.append(root.val)
    res.extend(inorder_traversal_1(root.right))
    
    return res

# doing it with helper method
def inorder_traversal_2(root):
    res = []
    
    def helper(node):
        if node is None:
            return
        helper(node.left)
        res.append(node.val)
        helper(node.right)
    
    helper(root)
    return res

# Test Case 1A: root = 1 -> right = 2 -> left = 3
#     1
#      \
#       2
#      /
#     3
node3 = TreeNode(3)
node2 = TreeNode(2, left=node3)
root1 = TreeNode(1, right=node2)
print(inorder_traversal_1(root1))  # Expected: [1, 3, 2]

# Test Case 1B: empty tree
root2 = None
print(inorder_traversal_1(root2))  # Expected: []

# Test Case 1C: single node
root3 = TreeNode(1)
print(inorder_traversal_1(root3))  # Expected: [1]

print()

# Test Case 1A: root = 1 -> right = 2 -> left = 3
#     1
#      \
#       2
#      /
#     3
node3 = TreeNode(3)
node2 = TreeNode(2, left=node3)
root1 = TreeNode(1, right=node2)
print(inorder_traversal_2(root1))  # Expected: [1, 3, 2]

# Test Case 1B: empty tree
root2 = None
print(inorder_traversal_2(root2))  # Expected: []

# Test Case 1C: single node
root3 = TreeNode(1)
print(inorder_traversal_2(root3))  # Expected: [1]