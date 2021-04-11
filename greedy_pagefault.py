class LRUCache:
    def __init__(self, cap):
        self.cache = []
        self.capacity = cap
        
    def sett(self, key, cnt):
        if len(self.cache)<self.capacity:
            self.cache.append(key)
        elif key not in self.cache:
            self.cache.pop(0)
            self.cache.append(key)
            cnt+=1
        
        return cnt
        
        
        
case = int(input())
for i in range(case):
    n = int(input())
    arr =list(map(int, input().split()))
    k = int(input())
    cache = LRUCache(k)
    count = k
    for i in arr:
        count = cache.sett(i, count)
    print(count)
