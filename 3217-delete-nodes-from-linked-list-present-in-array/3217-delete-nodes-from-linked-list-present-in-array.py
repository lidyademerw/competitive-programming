# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        x=set(nums)
        dummy = ListNode()
        dummy.next = head
        current = dummy
        while current.next is not None:
            if current.next.val in x:
                current.next=current.next.next
            else:
                current=current.next
        return dummy.next

        