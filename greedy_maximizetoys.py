def maximizeToys(arr, n, k):
    cost, count = 0, 0
    arr.sort()
    for i in range(n):
        if arr[i]<=k and cost<=k:
            cost+=arr[i]
            count+=1
    print(count)

case = int(input())
for i in range(case):
    n, k= list(map(int, input().split()))
    llist = list(map(int, input().split()))
    maximizeToys(llist, n, k)
