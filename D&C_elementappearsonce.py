def elementOnce(arr, n):
    
    count = [0 for x in range(n)]
    
    for i in arr:
        count[i] +=1
        
    for i in arr:
        if count[i]==1:
            print(i)
        


case = int(input())
for i in range(case):
    n = int(input())
    arr = list(map(int, input().split()))
    elementOnce(arr, n)
