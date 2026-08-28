class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        #hm will contain key:node
        self.hm = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        # print(self.hm)
        if key in self.hm:
            #update to most recently used
            node = self.hm[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            #now attach to the end
            temp = self.tail.prev
            self.tail.prev = node
            node.next = self.tail
            node.prev = temp
            temp.next = node
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            #now attach to the end --> right before tail
            temp = self.tail.prev
            self.tail.prev = node
            node.next = self.tail
            node.prev = temp
            temp.next = node
            node.val = value
        else:
            if len(self.hm) == self.capacity:
                #take out least recent --> right after head
                popped = self.head.next
                self.head.next = popped.next
                popped.next.prev = self.head
                del self.hm[popped.key]

            #now create node and attach to the end
            node = Node(key, value)
            self.hm[key] = node
            temp = self.tail.prev
            self.tail.prev = node
            node.next = self.tail
            node.prev = temp
            temp.next = node
            node.val = value



        
