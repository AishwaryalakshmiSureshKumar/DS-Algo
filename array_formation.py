def fun(arr,pieces):
    pieces_len = len(pieces)
    count=0
    i=0
    while i<pieces_len:
        if len(pieces[i])==1:
            if pieces[i][0] in arr:
                count+=1
            else:
                return False
        else:
            j=0
            k=-1
            while j<len(arr):
                if pieces[i][0]==arr[j]:
                    k=j+1
                    count+=1
                    break
                j+=1
            l=1
            if k>=0:
                while k<len(arr) and l<len(pieces[i]):
                    if arr[k]==pieces[i][l]:
                        l+=1
                        k+=1
                        count+=1
                    else:
                        return False
            else:
                return False
                
        i+=1
    if count==len(arr):
        return True
    return False

arr = [9,4,64,16]
pieces = [[16],[4,64],[9]]

print(fun(arr,pieces))

'''TestCase 1:
    arr = [85]
    pieces = [[85]]
    output: true

TestCase 2:
    arr = [88,15]
    pieces = [[15],[88]]
    output: true

TestCase 3:
    arr = [49,18,16]
    pieces = [[16,18,49]]
    output: false

TestCase 4:
    arr = [9,4,64,16]
    pieces = [[16],[4,64],[9]]
    output: true

TestCase 5:
    arr = [1,3,5,7]
    pieces = [[2,4,6,8]]
    output: false'''
