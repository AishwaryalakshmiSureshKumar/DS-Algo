
def max_sub_arr(arr, n, k):
    max_ = 0

    for i in range(n-k+1):
        max_ = arr[i]
        for j in range(1, k):
            if arr[i+j]>max_:
                max_ = arr[i+j]
        print(max_, end=' ')
    print()                                                                                   
               


test_case = int(input())
for i in range(test_case):
    elem = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    max_sub_arr(arr, elem[0], elem[1])
