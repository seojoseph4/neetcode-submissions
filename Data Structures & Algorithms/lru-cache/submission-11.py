class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        #key : node
        self.hm = {}
        self.capacity = capacity
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        res = self.hm[key]
        res.prev.next = res.next
        res.next.prev = res.prev
        
        temp = self.tail.prev
        self.tail.prev = res
        res.prev = temp
        res.next = self.tail
        temp.next = res
        return res.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            res = self.hm[key]
            res.prev.next = res.next
            res.next.prev = res.prev
            del self.hm[key]
        if len(self.hm) == self.capacity:
            lru = self.head.next
            lru.next.prev = self.head
            self.head.next = lru.next
            del self.hm[lru.key]

        res = ListNode(key, value)
        temp = self.tail.prev
        self.tail.prev = res
        res.prev = temp
        res.next = self.tail
        temp.next = res
        self.hm[key] = res

        
