#code
def Dist(str1, str2, n1, n2):

    T = [[0 for i in range(n1+1)] for j in range(n2+1)]
    
    for i in range(n2+1):
        for j in range(n1+1):
            if i==0:
                T[i][j] = j
            elif j==0:
                T[i][j] = i
            else:
                T[i][j] = 0
            
    
    if n1==0:
        return n2
        
    if n2==0:
        return n1
    
    for i in range(1, n2+1):
        for j in range(1, n1+1):
            if str1[j-1]==str2[i-1]:
                T[i][j] = min(T[i-1][j], T[i][j-1], T[i-1][j-1])+1
            else:
                T[i][j] = T[i-1][j-1]
                
    print(T)

case = int(input())
for i in range(case):
    n1, n2 = list(map(int, input().split()))
    str1, str2 = list(map(str, input().split()))
    Dist(str1, str2, n1, n2)
