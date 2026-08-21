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
        hm = defaultdict(lambda:Node(0))
        hm[None] = None
        res = head
        while head:
            hm[head].val = head.val
            hm[head].next = hm[head.next]
            hm[head].random = hm[head.random]
            head = head.next
        return hm[res]




            
        
        