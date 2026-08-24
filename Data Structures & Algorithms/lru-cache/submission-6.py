class Node:
    def __init__(self, key, val, next, prev):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.capacity = capacity
        self.head = Node(0,0, None, None)
        self.end = Node(0,0, None, None)
        self.head.next = self.end
        self.end.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hm:
            curr = self.hm[key]
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            temp = self.end.prev
            self.end.prev = curr
            curr.next = self.end
            curr.prev = temp
            temp.next = curr
            return self.hm[key].val
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.hm[key].prev.next = self.hm[key].next
            self.hm[key].next.prev = self.hm[key].prev
            del self.hm[key]
            
        if self.capacity < len(self.hm) + 1:
            del self.hm[self.head.next.key]
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next

        curr = Node(key,value, None, None)
        temp = self.end.prev
        self.end.prev = curr
        curr.next = self.end
        curr.prev = temp
        temp.next = curr
        if key in self.hm:
            self.hm[key].prev.next = self.hm[key].next
            self.hm[key].next.prev = self.hm[key].prev

        self.hm[key] = curr
        # print(self.hm)


        
