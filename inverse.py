
def inverse(arr, arrlen):
    count=0
    for i in range(arr_len-1):
        j=i+1
        for j in range(j, arr_len):
            if arr[j]<arr[i]:
                count+=1
                print(arr[i],arr[j])
    return count


test_case = int(input())
for i in range(test_case):
    arr_len = int(input())
    arr = [int(x) for x in input().split()]
    print(inverse(arr, arr_len))
