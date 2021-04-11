
def k_small_elem(a, k):
    a.sort()
    return a[k-1]


test_case = int(input())
for i in range(test_case):
    arr_len = int(input())
    arr=list(map(int, input().split()))
    k_elem = int(input())
    print(k_small_elem(arr, k_elem))
