#code
def minimizeSumProduct(list1, list2, llen):
    list1.sort()
    list2.sort(reverse=True)
    summ=0
    for i in range(llen):
        summ+= (list1[i]*list2[i])
        
    print(summ)


case = int(input())
for i in range(case):
    llen = int(input())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    minimizeSumProduct(list1, list2, llen)


'''2
3 
3 1 1
6 5 4
5
6 1 9 5 4
3 4 8 2 4'''
