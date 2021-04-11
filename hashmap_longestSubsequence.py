#code
def longestSubsequence(arr, n):
    count=0
    maxx = 0
    arr = sorted(arr)
    print(arr)
    for i in range(0,n):
        if i>0:
            if arr[i]==arr[i-1]+1:
                count+=1
            else:
                count=1
        else:
            count = 1

        maxx = max(maxx, count)
    print(maxx)


case = int(input())
for i in range(case):
    llen = int(input())
    llist = list(map(int, input().split()))
    longestSubsequence(llist, llen)
