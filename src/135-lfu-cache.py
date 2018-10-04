import bisect
class LFUCache(object):
    def __init__(self, capacity):
        self.clock = 0                     # to track least recent used
        self.key_arr = []                  # bisect array, to discard the least frequently used
        self.capacity = capacity
        self.h = {}    
    
    def get(self, key):
        if key in self.h:
            val, freq, clock  = self.h[key]
            self.key_arr.pop(bisect.bisect_left(self.key_arr, (freq, clock)))
            self.h[key] = (val, freq+1, self.clock)
            bisect.insort_left(self.key_arr, (freq+1, self.clock, key))
            self.clock += 1
            return val        
        return -1
            
    def put(self, key, value):
        if self.capacity ==0: return    
        if key in self.h:
            _, freq, clock = self.h[key]
            self.h[key] = (value, freq, clock)
            self.get(key)
        else:
            if len(self.h) == self.capacity:
                del self.h[self.key_arr[0][2]]
                self.key_arr.pop(0)
            self.h[key] = (value, 1, self.clock)
            bisect.insort_left(self.key_arr, (1, self.clock, key))
            self.clock += 1

cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)    
cache.get(2)       
cache.get(3)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)
