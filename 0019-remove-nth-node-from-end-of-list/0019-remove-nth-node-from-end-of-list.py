# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        count=0
        current=head
        while current is not None:
            count+=1
            current=current.next
        if n==count:
            return head.next
        prev=None
        current=head
        while count!=n:
            count-=1
            prev=current
            current=current.next

        prev.next=current.next
        return head


        
       
            



        