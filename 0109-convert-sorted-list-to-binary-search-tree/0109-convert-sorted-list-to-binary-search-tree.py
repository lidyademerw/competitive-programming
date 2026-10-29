# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        if head is None:
            return None
        def bst(l,r):
            if l==r:
                return None
            slow=l
            fast=l
            while fast!=r and fast.next!=r:
                slow=slow.next
                fast=fast.next.next
            root=TreeNode(slow.val)
            root.left=bst(l,slow)
            root.right=bst(slow.next,r)
            return root
        return bst(head,None)
    
        