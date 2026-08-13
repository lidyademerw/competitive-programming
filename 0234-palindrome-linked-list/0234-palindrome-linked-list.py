# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        pre=None
        current=slow
        while current is not None:
            temp=current.next
            current.next=pre
            pre=current
            current = temp  
        x=head
        while pre is not None and x is not None:
            if pre.val!=x.val:
                return False
            pre=pre.next
            x=x.next
        return True