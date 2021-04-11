def coinPiles(arr, n, k):
    count = 0

    minVal = arr[0]
    for i in range(1, n-1):
        diff = arr[i] - minVal
        minVal = arr[i]
        if diff>k:
            count += (diff-k)

    print(count)


case = int(input())
for i in range(case):
    n, k= list(map(int, input().split()))
    llist = list(map(int, input().split()))
    coinPiles(llist, n, k)
    


'''3
4 0
2 2 2 2
6 3
1 2 5 1 1 1
6 3
1 5 1 2 5 1'''
