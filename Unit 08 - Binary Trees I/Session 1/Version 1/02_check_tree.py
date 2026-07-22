class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    if root.val == root.left.val + root.right.val:
        return True
    return False

tree = TreeNode(10, TreeNode(4), TreeNode(6))
tree2 = TreeNode(5, TreeNode(3), TreeNode(1))

print(check_tree(tree))
print(check_tree(tree2))
