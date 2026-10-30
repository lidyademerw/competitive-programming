# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdi=0
        def diameter(root):
            if root is None:
                return 0
            left=diameter(root.left)
            right=diameter(root.right)
            x=left+right
            self.maxdi=max(x,self.maxdi)
            return 1+ max(right,left)
        diameter(root)
        return self.maxdi



        