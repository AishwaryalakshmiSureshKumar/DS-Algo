def printMaze(sol, n):

    for i in range(n):
        for j in range(n):
            print(sol[i][j],end=' ')
        print()


def isSafe(mat, x, y, n):

    if x>=0 and x<n and y>=0 and y<n and mat[x][y]==1:
        return True

    return False


def solveMazeUtil(mat, x, y, sol, n):

    if x==n-1 and y==n-1:
        sol[x][y]=1
        return True

    if isSafe(mat, x, y, n)==True:
        sol[x][y]=1

        if solveMazeUtil(mat, x+1, y, sol, n)==True:
            return True

        if solveMazeUtil(mat, x, y+1, sol, n)==True:
            return True

        sol[x][y]=0
        return False


def solveMaze(mat, n):

    sol = [[0 for j in range(n)] for i in range(n)]

    if solveMazeUtil(mat, 0, 0, sol, n)==False:
        print('-1')
        return False

    printMaze(sol, n)
    return True


case = int(input())
for i in range(case):
    n = int(input())
    arr = list(map(int, input().split()))
    mat = [[0 for i in range(n)] for j in range(n)]
    k=0
    for i in range(n):
        for j in range(n):
            mat[i][j]=arr[k]
            k+=1
    solveMaze(mat, n)
