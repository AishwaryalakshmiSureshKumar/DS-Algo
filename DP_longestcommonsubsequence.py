#code
def LCS(str1, str2, n1, n2):
    
    T = [[0 for i in range(n1+1)] for j in range(n2+1)]
    maxx=0
    
    for i in range(1, n2+1):
        for j in range(1, n1+1):
            if str1[j-1]==str2[i-1]:
                T[i][j] = T[i-1][j-1]+1
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
                
    print(T[n2-1][n1-1])

case = int(input())
for i in range(case):
    n1, n2 = list(map(int, input().split()))
    str1 = input()
    str2 = input()
    LCS(str1, str2, n1, n2)
