# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ancestor(root,p,q):
            if root is None or root==p or root==q:
                return root
            left=ancestor(root.left,p,q)
            right=ancestor(root.right,p,q)
            if left and right:
                return root
            return left if left else right
        return ancestor(root,p,q)
               

        