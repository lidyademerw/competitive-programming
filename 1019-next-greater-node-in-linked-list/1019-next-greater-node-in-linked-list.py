# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:
        res=[]
        current=head
        while current:
            res.append(current.val)
            current=current.next
        n=len(res)
        ans=[0]*n
        stack=[]
        for i in range(n):
            while stack and res[i] > res[stack[-1]]:
                ans[stack[-1]]=res[i]
                stack.pop()
            stack.append(i)
        return ans
    

     
        