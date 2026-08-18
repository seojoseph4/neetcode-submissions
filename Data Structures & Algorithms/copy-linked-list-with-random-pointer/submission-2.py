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
        hm = {}
        curr = head
        while curr:
            temp = Node(curr.val)
            hm[curr] = temp
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                hm[curr].next = hm[curr.next]
            else:
                hm[curr].next = None
            if curr.random:
                hm[curr].random = hm[curr.random]
            else:
                hm[curr].random = None
            curr = curr.next
        if head:
            return hm[head]
        else:
            return None
        
        