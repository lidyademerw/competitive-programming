# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        current=slow
        prev=None
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        head2=prev
        maxSum=0
        while head2:
            maxSum=max(maxSum,head.val+head2.val)
            head=head.next
            head2=head2.next
        return maxSum
        