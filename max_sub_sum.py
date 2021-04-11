import sys
INT_MIN = -sys.maxsize -1

def max_sub_sum(arr, n, k):
    max_sum = INT_MIN

    for i in range(n-k+1):
        current_sum = 0
        for j in range(k):
            current_sum+=arr[i+j]
        print(max(max_sum, current_sum))
    print()


test_case = int(input())
for i in range(test_case):
    elem = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    max_sub_sum(arr, elem[0], elem[1])
