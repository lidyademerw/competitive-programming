# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        x={}
        x[0]=1
        def dfs(root,currentSum):
            if not root:
                return 0
            currentSum+=root.val
            pathsum=0
            y=currentSum-targetSum
            if y in x:
                pathsum+=x[y]
            if currentSum in x:
                x[currentSum]+=1
            else:
                x[currentSum]=1
            pathsum+=dfs(root.left,currentSum)
            pathsum+=dfs(root.right,currentSum)
            x[currentSum]-=1
            return pathsum
        return dfs(root,0)


        
        