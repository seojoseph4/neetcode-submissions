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
        
        p1 = head

        while p1:
            dcopy = Node(p1.val)
            dcopy.next = p1.random
            p1.random = dcopy
            p1 = p1.next

        res = head.random if head else None
        p2 = head

        while p2:
            dcopy = p2.random
            dcopy.random = dcopy.next.random if dcopy.next else None
            p2 = p2.next
        
        p3 = head
        while p3:
            dcopy = p3.random
            realrandom = dcopy.next
            dcopy.next = p3.next.random if p3.next else None
            p3.random = realrandom
            p3 = p3.next
        return res

