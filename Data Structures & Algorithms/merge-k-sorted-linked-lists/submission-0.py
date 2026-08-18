# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minhp = []
        
        res= head = ListNode()
        for i in range(len(lists)):
            if list[i]:
                heapq.heappush(minhp, (lists[i].val, id(lists[i]), lists[i]))
        while minhp:
            curr = heapq.heappop(minhp)
            if curr[2].next:
                heapq.heappush(minhp, (curr[2].next.val, id(curr[2].next), curr[2].next))
            res.next = curr[2]
            res = res.next
        return head.next

        