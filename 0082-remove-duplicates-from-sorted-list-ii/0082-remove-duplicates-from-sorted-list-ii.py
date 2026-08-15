# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        if head is None or head.next is None:
            return head
        current=head 
        while current is not None and current.next is not None:
            if current.val!=current.next.val:
                prev=current
            else:
                while current.next is not None and current.val==current.next.val:
                    current.next=current.next.next
                    prev.next=current.next
            current=current.next
        return dummy.next
        
