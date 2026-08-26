# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head
        fast = head
        res = head

        groupprev = None
        gap = 0
        while fast:
            gap+=1
            if gap == k:
                next_group = fast.next
                prev = next_group
                curr = slow
                while curr != next_group:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                if groupprev == None:
                    res = fast
                
                if groupprev:
                    groupprev.next = fast
                groupprev = slow
                slow = next_group
                fast = next_group
    
                gap = 0
            else:
                fast = fast.next
        
        return res

