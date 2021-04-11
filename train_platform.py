
def plat_needed(arr, dep, n):
    arr.sort()
    dep.sort()
    i=1
    j=0
    result =1
    plat =1
    while(i<n and j<n):
        if(arr[i]<=dep[j]):
            plat+=1
            i+=1
        elif(arr[i]>dep[j]):
            plat-=1
            j+=1
        if result<plat:
            result=plat
    return result

test_case=int(input())
for i in range(test_case):
    arr_len = int(input())
    arr=list(map(int, input().split()))
    dep = list(map(int, input().split()))
    print(plat_needed(arr, dep, arr_len))
