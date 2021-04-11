#code
def pairswithSum(arr1, arr2, n1, n2, k):
    res = []
    for i in range(n1):
        
        for j in range(n2):
            
            if arr1[i]+arr2[j]==k:
                res.append([arr1[i], arr2[j]])

    res = sorted(res)
    k=1
    if res:
        for item in res:
            for i in item:
                if k%2==0:
                    if k==2*len(res):
                        print(i)
                        k+=1
                    else:
                        print(i, end=', ')
                        k+=1
                else:
                    print(i, end=' ')
                    k+=1
    else:
        print('-1')


case = int(input())
for i in range(case):
    len1, len2, summ = list(map(int, input().split()))
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    pairswithSum(list1, list2, len1, len2, summ)
