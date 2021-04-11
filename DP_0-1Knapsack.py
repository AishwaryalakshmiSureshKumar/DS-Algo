#code
def Knapsack(m, n, val, wt):
    
    T = [[0 for i in range(m+1)] for j in range(n)]
    
    for i in range(n):
        for j in range(1, m+1):
            if j<wt[i]:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(val[i]+T[i-1][j-wt[i]], T[i-1][j])
                
    print(T[n-1][m])


case = int(input())
for i in range(case):
    n = int(input())
    maxx = int(input())
    val = list(map(int, input().split()))
    wt = list(map(int, input().split()))
    Knapsack(maxx, n, val, wt)
