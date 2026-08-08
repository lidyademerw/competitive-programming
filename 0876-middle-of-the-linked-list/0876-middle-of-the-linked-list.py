# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        count=0
        while current is not None:
            count+=1
            current=current.next
        mid=count//2
        length=0
        current=head
        while length!=mid:
            length+=1
            current=current.next
        return current
            


        