#code
def LCS(str1, str2, n1, n2):

    maxx=0
    T = [[0 for j in range(n1)] for i in range(n2)]
    for i in range(n2):
        for j in range(n1):
            if str1[j]==str2[i]:
                T[i][j] = T[i-1][j-1]+1
            else:
                T[i][j] = 0
    print(T)
    for i in range(n2):
        for j in range(n1):
            if maxx<T[i][j]:
                maxx=T[i][j]

    print(maxx)
        


case = int(input())
for i in range(case):
    n1, n2 = list(map(int, input().split()))
    str1 = input()
    str2 = input()
    LCS(str1, str2, n1, n2)
