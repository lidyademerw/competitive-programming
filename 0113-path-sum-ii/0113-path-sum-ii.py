# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
            if root is None:
                return []
            if root.left is None and root.right is None:
                if targetSum==root.val:
                    return[[root.val]]
                else:
                    return[]
                res.append(path)
            left=self.pathSum(root.left,targetSum-root.val)
            right=self.pathSum(root.right,targetSum - root.val)
            res=[]
            for i in left + right:
                res.append([root.val]+i)
            return res
       
        