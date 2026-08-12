# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        prev=None
        if head is None or head.next is None:
            return head
        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        x=self.sortList(head)
        y=self.sortList(slow)
        dummy=ListNode()
        tail=dummy
        while x is not None  and y is not None:
            if  x.val <  y.val:
                tail.next=x
                x= x.next
            else:
                tail.next = y
                y= y.next
            tail=tail.next
        if  x:
            tail.next = x
        else:
            tail.next = y
        return dummy.next

        



        