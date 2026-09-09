# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevTail = dummy

        while True:
            kth = prevTail
            i = 0
            while kth and i < k:
                kth = kth.next
                i+=1
            if not kth:
                break
            nextHead = kth.next


            #reverse
            prev = nextHead
            curr = prevTail.next
            while curr != nextHead:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prevTail.next
            prevTail.next = kth
            prevTail = temp
        return dummy.next 





                
