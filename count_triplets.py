
def count(len, arr):
    count = 0
    for i in range(len-1):
        for j in range(i+1, len):
            sum = arr[i]+arr[j]
            if sum in arr:
                count=count+1
            else:
                continue
                
    if count==0:
        return -1
    else:
        return count
			

test_case = int(input())
for i in range(test_case):
	elem_len = int(input())
	temp=[int(x) for x in input().split()]
	print(count(elem_len, temp))