def swapPairs(list1, list2, l1, l2):
    
    sum1 = sum(list1)
    sum2 = sum(list2)
    
    diff = (sum1-sum2)//2
    flag=0
    
    if l1>l2:
        for i in list2:
            if i+diff in list1:
                flag=1
                break
    else:
        for i in list1:
            if i+diff in list2:
                flag=1
                break
            
    if flag:
        print('1')
    else:
        print('-1')
        
    
    
case = int(input())
for i in range(case):
    l1, l2 = list(map(int, input().split()))
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    swapPairs(list1, list2, l1, l2)
