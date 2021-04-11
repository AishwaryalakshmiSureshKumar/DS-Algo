
'''def missing_num(arr, arr_len):
    num=0
    for i in range(arr_len+1):
        if i not in arr:
            num = i
    return num

test_case = int(input())
for i in range(test_case):
    arr_len = int(input())
    arr=[int(x) for x in input().split()]
    print(missing_num(arr, arr_len))'''



n= int(input())
a =list(map(int, input().split()))

sum= (n*(n+1))//2
s=0
for i in a:
    s=s+i
mn=sum-s
print(mn)
