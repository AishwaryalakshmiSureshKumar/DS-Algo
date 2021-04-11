
def merge(arr1, arr2):
    arr = arr1+arr2
    arr.sort()
    return arr

test_case = int(input())
for i in range(test_case):
    arr_len = [int(arr_len) for arr_len in input().split()]
    arr1=[int(x) for x in input().split()]
    arr2=[int(x) for x in input().split()]
    res = merge(arr1, arr2)
    for i in range(len(res)-1):
            print(res[i],end=' ')
    print(res[len(res)-1])
