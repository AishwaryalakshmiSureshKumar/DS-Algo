#code
def coinChange(arr, n, k):
    
    T = [[0] * (k + 1) for x in range(n + 1)]

    for i in range(n+1):
        T[0][i] = 1
        
    for i in range(1, n+1):
        for j in range(1, k+1):
            if arr[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] + T[i][j-arr[i-1]]

    print(T[n][k])
                
    


case = int(input())
for i in range(case):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    coinChange(arr, n, k)
