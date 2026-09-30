# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy=ListNode()
        dummy.next=head
        tail=dummy
        current=head
        while current and current.next:
            swap1=current
            swap2=current.next
            swap1.next=swap2.next
            swap2.next=swap1
            tail.next=swap2
            tail=swap1
            current=swap1.next
        return dummy.next