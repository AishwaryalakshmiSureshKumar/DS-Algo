from itertools import permutations

def permutationList(s):
    pList = permutations(s)
    asc_list = []
    
    for p in pList:
        asc_list.append(''.join(p))
    asc_list.sort()
    return(asc_list)

'''res = []
def allPermutations(data, i, n):
    if i==n:
        res.append(''.join(data))
    else:
        for j in range(i,n):
            data[i], data[j] = data[j], data[i]
            allPermutations(data, i+1, n)
            data[i], data[j] = data[j], data[i]
    return str(res)'''


test_case = int(input())
for i in range(test_case):
    str1 = input()
    res = permutationList(str1)
    for i in res:
        print(i, end=' ')
    print()
    #result = allPermutations(list(str1), 0, len(str1))
    #print(result)
