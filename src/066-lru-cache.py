class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            n = self.dict[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self._remove(self.dict[key])
        n = Node(key, value)
        self.dict[key] = n
        self._add(n)
        if len(self.dict) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dict[n.key]
            
    def _remove(self, n):
        n.prev.next, n.next.prev = n.next, n.prev
        
    def _add(self, n):
        self.tail.prev.next, self.tail.prev, n.prev, n.next = n, n, self.tail.prev, self.tail


s = LRUCache(2)
s.put(1, 10)
s.put(2, 15)
print(s.get(1))
print(s.get(2))
print(s.get(10))
s.put(6, 14)
print(s.get(1))
