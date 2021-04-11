#code
def repeatandmiss(arr, n):
    arr.sort()
    print(arr)
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            print(arr[i], end=' ')
            break
    
    for i in range(1, n+1):
        if i not in arr:
            print(i)
            break


case = int(input())
for i in range(case):
    n = int(input())
    llist = list(map(int, input().split()))
    repeatandmiss(llist, n)
