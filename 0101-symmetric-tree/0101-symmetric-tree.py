# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        def symmetric(t1,t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None and t2 is not None:
                return False
            if t1 is not None and t2 is None:
                return False
            if t1.val!=t2.val:
                return False
            return symmetric(t1.left,t2.right) and symmetric(t1.right,t2.left)
        return symmetric(root.left,root.right)

        