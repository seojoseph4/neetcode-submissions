# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        
        #half
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #disconnect
        p2 = slow.next
        slow.next = None

        #reverse second half
        prev=None
        while p2:
            temp = p2.next
            p2.next = prev
            prev = p2
            p2 = temp
        

        p1 = head
        p2 = prev
        curr = dummy
        while p1 and p2:
            temp1 = p1.next
            temp2 = p2.next
            curr.next = p1
            curr = curr.next
            curr.next = p2
            curr = curr.next
            p1 = temp1
            p2 = temp2
        if p2:
            curr.next = p2
        
        


        

            


