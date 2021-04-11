
def leaders_arr(a, al):
    res = []
    r = 0
    for i in range(1, al):
        #print(a[i])
        count=-1
        for j in range(r, i):
            #print(a[j])
            if arr[i]<arr[j]:
                count+=1
                if count==j:
                    res.append(arr[i])
                    r = i+1


test_case = int(input())
for i in range(test_case):
    arr_len = int(input())
    arr=list(map(int, input().split()))
    res = leaders_arr(arr, arr_len)
    for i in res:
        print(i, end=' ')
    print()
