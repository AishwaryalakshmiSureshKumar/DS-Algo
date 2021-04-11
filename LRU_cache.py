from collections import OrderedDict

class Cache:

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache: 
            return -1
        else: 
            self.cache.move_to_end(key) 
            return self.cache[key] 

    def put(self, key, value): 
        self.cache[key] = value 
        self.cache.move_to_end(key) 
        if len(self.cache) > self.capacity: 
            self.cache.popitem(last = False)
        

test_case = int(input())
for i in range(test_case):
    capacity = int(input())
    cases = int(input())
    arr = list(input().strip().split())
    LRUCache = Cache(capacity)
    while i<len(arr):
        if arr[i]=='SET':
            LRUCache.put(arr[i+1], arr[i+2])
            i+=3
        elif arr[i]=='GET':
            print(LRUCache.get(arr[i+1]), end=' ')
            i+=2
                
    
