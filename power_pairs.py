#code
def power_fn(a1, a2, a_l):
    count=0
    for i in range(a_l[0]):
        for j in range(a_l[1]):
            if pow(i,j)>pow(j,i):
                count+=1
    return count


test_case = int(input())
for i in range(test_case):
    arr_len = [int(x) for x in input().split()]
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    print(power_fn(arr1, arr2, arr_len))
