# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def helper(li1, li2):
            res = ListNode(0)
            curr = res
            while li1 and li2:
                if li1.val < li2.val:
                    curr.next = li1
                    li1 = li1.next
                else:
                    curr.next = li2
                    li2 = li2.next
                curr = curr.next
            if li1:
                curr.next = li1
            elif li2:
                curr.next = li2
            return res.next
        stack = lists

        while len(stack) >1:
            l1 = stack.pop()
            l2 = stack.pop()
            stack.append(helper(l1,l2))
    
        return stack[0] if stack else None
