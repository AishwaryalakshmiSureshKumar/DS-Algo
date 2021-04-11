def CommonElements(L1, L2, L3, LN):
    result = []
    if LN[0]>=LN[1] and LN[0]>=LN[2]:
        llen = LN[0]
        for i in L1:
            if i in L2 and i in L3:
                result.append(i)
    elif LN[1]>=LN[0] and LN[1]>=LN[2]:
        llen = LN[1]
        for i in L2:
            if i in L1 and i in L3:
                result.append(i)
    elif LN[2]>=LN[0] and LN[2]>=LN[1]:
        llen = LN[2]
        for i in L3:
            if i in L1 and i in L2:
                result.append(i)
                
    if result:
        for i in result:
            print(i, end=' ')
    else:
        print('-1')
        
        
        

case = int(input())
for i in range(case):
    llen = list(map(int, input().split()))
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    list3 = list(map(int, input().split()))
    CommonElements(list1, list2, list3, llen)
