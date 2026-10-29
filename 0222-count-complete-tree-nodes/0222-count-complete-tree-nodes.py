# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        def right(root):
            level=0
            while root:
                root=root.right
                level+=1
            return level
        def left(root):
            level=0
            while root:
                root=root.left
                level+=1
            return level
        def count(root):
            levelright=right(root)
            levelleft=left(root)
            if levelright==levelleft:
                return pow(2,levelleft)-1
            else:
               return 1+count(root.right)+count(root.left)
        return count(root)



        
