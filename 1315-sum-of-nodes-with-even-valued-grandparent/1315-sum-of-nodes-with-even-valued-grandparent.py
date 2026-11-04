# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        self.res=0
        def dfs(cur,par,gp):
            if cur is None:
                return 
            if gp and gp.val%2==0:
                self.res+=cur.val
            dfs(cur.left,cur,par)
            dfs(cur.right,cur,par)
        dfs(root,None,None)
        return self.res


        

        