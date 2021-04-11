
def equilibrium(a, al):
    point=0
    res = sum(a)
    sum1= 0
    if al==1:
        point=1
    else:
        for i in range(al):
            sum1 = sum1 + arr[i]
            if sum1==res:
                point = i+1
            else:
                res = res - arr[i]
    if point==0:
        return -1
    else:
        return point

test_case = int(input())
for i in range(test_case):
    arr_len = int(input())
    arr = [int(x) for x in input().split()]
    print(equilibrium(arr, arr_len))
