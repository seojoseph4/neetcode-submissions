"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hm = {}
        res = copyhead = Node(head.val)
        r2 = head
        while head:
            hm[head] = copyhead
            copyhead.next = Node(head.next.val) if head.next else None
            head = head.next
            copyhead = copyhead.next

        while r2:
            hm[r2].random = hm[r2.random] if r2.random else None
            r2=r2.next
        return res




            
        
        