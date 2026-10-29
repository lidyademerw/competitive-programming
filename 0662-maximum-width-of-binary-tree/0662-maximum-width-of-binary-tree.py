# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        queue=deque([(root,0)])
        if root is None:
            return 0
        maxwid=0
        while queue:
            l=queue[0][1]
            r=queue[-1][1]
            maxwid=max(maxwid,r-l+1)
            for i in range(len(queue)):
                node,ind=queue.popleft()
                if node.left:
                    queue.append((node.left,2*ind))
                if node.right:
                    queue.append((node.right,2*ind+1))
        return maxwid
  
            
        