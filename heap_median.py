#code
from heapq import heappush, heappop, heapify
maxh = []
minh = []
def median_in_stream(ll):
    
    for val in ll:
        if not maxh and not minh:
            maxh.append(val)
        elif maxh:
            if val>=maxh[0]:
                minh.append(val)
            elif val<maxh[0]:
                maxh.append(val)

        if len(maxh)==len(minh):
            print((maxh[0]+minh[0])//2)
        elif len(maxh)==len(minh)+1:
            print(maxh[0])
        elif len(minh)==len(maxh)+1:
            print(minh[0])
        elif len(minh)==len(maxh)+2:
            heappush(maxh, minh[len(minh)-1])
            print((maxh[0]+minh[0])//2)
        elif len(maxh)==len(minh)+2:
            heappush(minh, maxh[len(maxh)-1])
            print((maxh[0]+minh[0])//2)
    
    
    
test_case = int(input())
list_ = []
for i in range(test_case):
    elem = list_.append(int(input()))
median_in_stream(list_)
