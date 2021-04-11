def allfourSum(llist, k, llen):
    
    for i in range(llen):
        curr_sum = 0
        ll=[]

        for j in range(i, llen):
            curr_sum += llist[j]
            ll.append(llist[j])
            
            if curr_sum==k and len(ll)==4:
                ll=sorted(ll)
                for i in range(len(ll)):
                    print(ll[i], end=' ')

                print('$')
    
    
            

case= int(input())
for i in range(case):
    llen, k = list(map(int, input().split()))
    llist = list(map(int, input().split()))
    allfourSum(llist, k, llen)
    print()
