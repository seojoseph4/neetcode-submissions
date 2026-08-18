class Node:
    def __init__(self, key: int, val: int, next: 'Node' = None, prev: 'Node' = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = {}
        self.cap = capacity
        self.tail = Node(0,0)
        self.head = Node(0,0)
        self.tail.prev = self.head
        self.head.next = self.tail

    def remove(self, curr: Node):
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.next = None
        curr.prev = None
    def update(self, curr: Node):
        self.tail.prev.next = curr
        curr.prev = self.tail.prev
        curr.next = self.tail
        self.tail.prev = curr
    def get(self, key: int) -> int:
        if key in self.mapping:
            self.remove(self.mapping[key])
            self.update(self.mapping[key])
            return self.mapping[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.mapping[key].val = value
            self.remove(self.mapping[key])
            self.update(self.mapping[key])
        else:
            if len(self.mapping) >= self.cap:
                LRU = self.head.next
                self.remove(LRU)
                del self.mapping[LRU.key]
            curr = Node(key, value)
            self.mapping[key] = curr
            self.update(curr)



        
