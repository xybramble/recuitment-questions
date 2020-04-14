'''
用栈模拟递归
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node:
                temp = node.left
                node.left = node.right
                node.right = temp
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return root
'''
另一种：交换左右子树的值，再递归左右子树
每个节点只访问一次，时间复杂度O(n)，空间复杂度O(n)（树完全不平衡，只有左子树）或O(log(n))（树完全平衡，递归调用logn(2*n)次）
'''
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        else:
            root.left, root.right = root.right, root.left
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
        return root
