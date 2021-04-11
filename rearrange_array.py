def rearrange(arr, arr_len):
    new_arr =[]
    i,j=0,len(arr)-1
    while(j>=i):
        if(i==j):
            new_arr.append(arr[i])
        else:
            new_arr.append(arr[j])
            new_arr.append(arr[i])
        i+=1
        j-=1
    return new_arr

test_case = int(input())
for i in range(test_case):
    arr_len = int(input())
    arr=[int(x) for x in input().split()]
    res = rearrange(arr,arr_len)
    for i in res:
        print(i, end=' ')
    print()
