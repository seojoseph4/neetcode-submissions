# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        pointer = ListNode()
        res = pointer
        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                temp = list1.next
                list1.next = None
                list1 = temp
            else:
                pointer.next = list2
                temp = list2.next
                list2.next = None
                list2 = temp
            pointer = pointer.next
        
        if list1:
            pointer.next = list1
        elif list2:
            pointer.next = list2
        
        return res.next


        