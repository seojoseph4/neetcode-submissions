# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        middle = head
        second = head
        while second and second.next:
            middle = middle.next
            second = second.next.next
        half = middle.next
        middle.next = None
        # print(middle.val)
        dummy = None
        while half:
            temp = half.next
            half.next = dummy
            dummy = half
            half = temp
        # print(dummy.val)
        # print(head.val)

        while dummy and head:
            temp1 = head.next
            temp2 = dummy.next
            head.next = dummy
            dummy.next = temp1
            head = temp1
            dummy = temp2


        


        