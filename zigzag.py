
def zigzag(a, l):
    i=0
    while i<l-1:
        if i==0 or i%2==0:
            if a[i]<a[i+1]:
                i+=1
                continue
            else:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                i+=1
        else:
            if a[i]>a[i+1]:
                i+=1
                continue
            else:
                temp=a[i]
                a[i]=a[i+1]
                a[i+1] = temp
                i+=1
    return a


test_case = int(input())
for i in range(test_case):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    res = zigzag(arr, arr_len)
    for i in res:
        print(i, end=' ')
    print()
