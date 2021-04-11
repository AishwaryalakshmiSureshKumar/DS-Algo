#code
def numberofPaths(r, c):

    if r==1 or c==1
        return 1

    return numberofPaths(r-1, c) + numberofPaths(r, c-1)
    
    
test_case = int(input())
for i in range(test_case):
    r, c = list(map(int, input().split()))
    numberofPaths(r, c)
