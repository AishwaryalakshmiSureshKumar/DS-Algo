
def pythagorean(a, l):
    flag=0
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(i+2, l):
                summ = pow(i,2)+pow(j,2)
                if summ==pow(k,2):
                    flag=1
    if flag==1:
        return "Yes"
            

test_case = int(input())
for i in range(test_case):
    arr_len = int(input())
    arr=list(map(int, input().split()))
    print(pythagorean(arr, arr_len))
