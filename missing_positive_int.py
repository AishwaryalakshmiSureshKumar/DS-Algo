def fun(arr, k):
    i = 1
    n = len(arr)
    count = 0
        
    while i<=arr[n-1]+k:
        print(i)
        if i not in arr:
            count+=1
        if count==k:
            break
        i+=1
    return i

arr = [1,2,3,4]
k = 2
print(fun(arr,k))
