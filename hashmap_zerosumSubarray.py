def zeroSum(arr, n):
    count = 0
    for i in range(n):
        summ = arr[i]
        if summ==0:
            count+=1
        for j in range(i, n):
            summ += arr[j]
            if summ==0:
                count+=1
    print(count)
    


case = int(input())
for i in range(case):
    llen = int(input())
    llist = list(map(int, input().split()))
    zeroSum(llist, llen)
