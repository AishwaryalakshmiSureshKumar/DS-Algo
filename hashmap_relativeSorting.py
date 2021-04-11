

def relativeSorting(L1, L2, len1, len2):

    freq = {}

    for i in L1:
        freq[i] = freq.get(i, 0) + 1

    arr = sorted(L1)

    for i in L2:
        if i in L1:
            k=0
            while k<freq.get(i):
                print(i, end=' ')
                k+=1
                arr.remove(i)

    if arr:
        for i in arr:
            print(i, end=' ')
                
        


case = int(input())
for i in range(case):
    a_len, b_len = list(map(int, input().split()))
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    hashmap = [[], ]*a_len
    
    relativeSorting(alist, blist, a_len, b_len)
    print()
