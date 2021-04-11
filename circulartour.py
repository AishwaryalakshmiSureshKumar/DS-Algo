'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''
#Your task isto complete this function
#Your function should return the starting point
def tour(lis, n):
    #Code here
    i=0
    balance_petrol = lis[i][0]

    start = 0
    while i<n:
        if balance_petrol<lis[i][1]:
            balance_petrol = lis[i+1][0]
            start = i+1
            i+=1
        else:
            balance_petrol = (balance_petrol-lis[i][1])
            
            if i<(n-1):
                balance_petrol = balance_petrol + lis[i+1][0]
            i+=1
        
    if (balance_petrol+lis[start][0])>lis[start][1]:
        return start
    return '-1'
            


#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends
