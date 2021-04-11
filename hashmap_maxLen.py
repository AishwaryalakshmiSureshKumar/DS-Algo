
def maxLen(n, arr):
    #Code here
    max_len = 0
    for i in range(len(arr)):
        
        curr_sum = 0
        
        for j in range(i, len(arr)):
            curr_sum +=arr[j]
            if curr_sum == 0:
                max_len = max(max_len, j-i+1)
                
    return max_len
    
            
    


case = int(input())
for i in range(case):
    llen = int(input())
    llist = list(map(int, input().split()))
    print(maxLen(llen, llist))
