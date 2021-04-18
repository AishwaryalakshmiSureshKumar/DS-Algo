def fun(instructions):
    nums = []
    res = 0
    for i in instructions:
        nums.append(i)
        count1 = 0 
        count2 = 0
        for k in nums:
            if k<i:
                count1+=1
            elif k>i:
                count2+=1
        res+=min(count1,count2)
        print(res)
                
    return res

instructions = [1,5,6,2]
print(fun(instructions))
