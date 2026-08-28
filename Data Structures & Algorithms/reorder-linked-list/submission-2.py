# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        #find half
        slow = head
        fast = head
        while fast and fast.next:
            b4slow = slow
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        p2 = slow.next
        slow.next = None

        prev = None
        while p2:
            temp = p2.next
            p2.next = prev
            prev = p2
            p2 = temp
        
        #start of first half: head
        #start of second half reverse: prev

        h1 = head
        h2 = prev
        curr = ListNode(0)
        while h1 and h2:
            temp1 = h1.next
            temp2 = h2.next
            h1.next = h2
            curr.next = h1
            curr = h2
            h1 = temp1
            h2 = temp2
        if h1:
            curr.next = h1
            


