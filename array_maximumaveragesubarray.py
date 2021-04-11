def average(arr, i, j, k):
        avg=0
        for x in range(i,j):
            print(arr[x])
            avg= avg+arr[x]
        #print(avg/4)
        return (avg/k)
    
def findMaxAverage(nums, k):
        
    avg = nums[0]
    max_avg = -10000
    n= len(nums)
    i,j=0,0
        
    if k==1:
        return max(nums)
    else:
        while j+k-1<n:
            res = average(nums, i, j+k, k)
            if res>max_avg:
                max_avg=res
            i+=1
            j+=1
    return max_avg

inp = [3,3,4,3,0]
k=3
print(findMaxAverage(inp,k))
