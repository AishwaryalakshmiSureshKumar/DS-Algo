import heapq

class KthLargest:

    def __init__(self, k: 'int', nums: 'List[int]'):
        self.data = nums
        heapq.heapify(self.data)
        self.k = k
        while len(self.data) > k:
            heapq.heappop(self.data)
        

    def add(self, val: 'int') -> 'int':
        if len(self.data) < self.k:
            heapq.heappush(self.data, val)
            print(self.data[0], end=' ')
        
        if val > self.data[0]:
            heapq.heapreplace(self.data, val)
        print(self.data[0])
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
case = int(input())
for i in range(case):
    target, llen = list(map(int, input().split()))
    llist = list(map(int, input().split()))
    obj = KthLargest(target, llist)
    for i in llist:
        obj.add(i)
