# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        res = ListNode()
        out = res
        hp = []
        # each element = value, [which list, index within the list]

        for i in range(len(lists)):
            #tie case cant compare nodes directly
            if lists[i]:
                heapq.heappush(hp,[lists[i].val,hash(lists[i]), lists[i]])
        
        while hp:
            current = heapq.heappop(hp)[2]
            if current:
                res.next =current
                res = res.next
                if current.next:
                    heapq.heappush(hp, [current.next.val, hash(current.next), current.next])

        return out.next
