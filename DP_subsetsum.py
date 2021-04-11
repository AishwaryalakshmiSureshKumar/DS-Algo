#code
def subsetSum(n, val, m):
    
    T = [[0 for i in range(m+1)] for i in range(n)]
    for i in range(n):
        T[i][0]=1
    
    for i in range(n):
        for j in range(1, m+1):
            if j<val[i]:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j-val[i]]

    if T[n-1][m]:
        print('YES')
    else:
        print('NO')


case = int(input())
for i in range(case):
    n = int(input())
    val = list(map(int, input().split()))
    maxx = 0
    for i in val:
        if maxx<i:
            maxx=i
    subsetSum(n, val, maxx)
