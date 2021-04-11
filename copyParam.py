import copy

strr = 'aishwarya'
a = list(strr[0:5])
temp = copy.copy(a)
if temp==a:
    print("Yes")
