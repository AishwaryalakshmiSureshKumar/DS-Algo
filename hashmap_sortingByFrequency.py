from collections import Counter

def sortingByFreq(llist, llen):

    llist.sort()
    llist = sorted(llist, key=llist.count, reverse=True)
    for i in llist:
        print(i, end=' ')

    
    
case = int(input())
for i in range(case):
    llen = int(input())
    llist = list(map(int, input().split()))
    sortingByFreq(llist, llen)
