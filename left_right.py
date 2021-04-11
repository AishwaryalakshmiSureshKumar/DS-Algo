#code

def left_right(a, l):
    i=0
    j=1
    res = []
    while j<l-2:
        if(a[j]>a[j-1] and a[j]<a[j+1]):
            res.append(a[j])
            j+=1
        else:
            j+=1
    if res:
        return res[-1]
    else:
        return -1


test_case = int(input())
for i in range(test_case):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    print(left_right(arr, arr_len))
