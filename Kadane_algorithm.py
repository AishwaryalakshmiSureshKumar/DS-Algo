def kadane_fn(arr, len):
	max_sum = 0
	for i in range(arr_len-1):
		summ=arr[i]
		for j in range(i+1, len):
			summ = summ+arr[j]
			if summ>max_sum:
                max_sum=summ
        if max_sum==0:
            max_num = 0
            for i in arr:
                if i>max_num:
                    max_num=i
            return max_num
        else:
            return max_sum
			

test_case = int(input())
for i in range(test_case):
	arr_len = int(input())
	arr=[int(x) for x in input().split()]
	print(kadane_fn(arr, arr_len))
