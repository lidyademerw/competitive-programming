# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        self.sum=0
        def dfs(root,current):
            current=current*10 + root.val
            if root.left is None and root.right is None:
                self.sum+=current
            if root.left:
                dfs(root.left,current)
            if root.right:
                dfs(root.right,current)
        dfs(root,0)
        return self.sum

            
