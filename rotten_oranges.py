
def rotten_orange(m, n):
    count=0
    for i in range(num_elems[0]-1):
        for j in range(num_elems[1]-1):
            if m[i][j]==2:
                if m[i+1][j]==1:
                    m[i+1][j]=2
                    flag=1
                if m[i-1][j]==1:
                    m[i-1][j]=2
                    flag=1
                if m[i][j-1]==1:
                    m[i][j-1]=2
                    flag=1
                if m[i][j+1]==1:
                    m[i][j+1]=2
                    flag=1
            if flag==1:
                count+=1
                flag=0
    return count

test_case = int(input())
for i in range(test_case):
    num_elems = list(map(int, input().split()))
    arr = list(map(int, input().strip().split()))
    mat = []
    for i in range(num_elems[0]):
        l = []
        k=0
        for j in range(num_elems[1]):
            l.append(arr[k])
            k+=1
        mat.append(l)
        k+=num_elems[1]
    print(rotten_orange(mat, num_elems))
        
        
