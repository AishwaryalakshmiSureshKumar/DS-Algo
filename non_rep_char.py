
test_case = int(input())
for i in range(test_case):
    num_elems = list(int(input()))
    arr = list(map(int, input().strip().split()))
    mat = []
    for i in range(num_elems[0]):
        k=0
        for j in range(num_elems[1]):
            mat(i,j) = arr[k]
        k+=num_elems[1]
        
        
