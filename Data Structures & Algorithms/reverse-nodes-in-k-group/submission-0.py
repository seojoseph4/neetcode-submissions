# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        total = 0
        curr = head
        while curr!=None:
            total+=1
            curr = curr.next
        
        groups = total // k
        # print(groups)

        dummy = ListNode()
        prevTail = dummy
        curr = head
        while groups > 0:
            grouphead = curr
            groupprev = None

            index = 0
            while index < k and curr!=None:
                #print(curr.val)
                temp = curr.next
                curr.next = groupprev
                groupprev = curr
                curr = temp
                index+=1
            
            prevTail.next = groupprev
            grouphead.next = curr
            prevTail = grouphead

            groups -=1
        return dummy.next






        