# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast= head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        p1 = head
        p2 = prev
        res = ListNode()
        while p1 and p2:
            tmp1 = p1.next
            tmp2 = p2.next
            res.next = p1
            res = res.next
            res.next = p2
            res = res.next
            p1 = tmp1
            p2 = tmp2
        if p1:
            res.next = p1




        


        