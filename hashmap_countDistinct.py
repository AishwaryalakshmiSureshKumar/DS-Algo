def countDistinctUtil(i, k, arr, freq):
    count = 0
    j=i
    res = []
    while j<(k+i):
        if freq[arr[j]]==1:
            count+=1
        elif freq[arr[j]]>1 and arr[j] not in res:
            count+=1
            res.append(arr[j])
        j+=1
    return count


def countDistinct(arr, n, k):
    freq = {}
    
    for i in arr:
        freq[i] = freq.get(i, 0)+ 1
    i=0
    result = []
    while i<=(n-k):
        result.append(countDistinctUtil(i, k, arr, freq))
        i+=1
    return result
    
    
            

t= int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    res = countDistinct(arr, n, k)
    for i in res:
        print(i, end=' ')
    print()
