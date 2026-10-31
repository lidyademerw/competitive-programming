"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        def dfs(node):
            cur=node
            tail=node
            while cur:
                temp=cur.next
                if cur.child:
                    childtail=dfs(cur.child)
                    cur.next=cur.child
                    cur.child.prev=cur
                    if temp:
                        childtail.next=temp
                        temp.prev=childtail
                    cur.child=None
                    tail=childtail
                else:
                    tail=cur
                    cur=temp
            return tail
        dfs(head)
        return head
         
       
        