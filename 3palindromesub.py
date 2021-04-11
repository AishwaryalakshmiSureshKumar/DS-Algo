def checkPalindrome(st, en, strr):
    stack = []
    count = 0
    res =[]
    for i in range(st, en):
        stack.append(strr[i])

    for i in range(st, en):
        if strr[i]!=stack.pop():
            count+=1
        else:
            res.append(strr[i])

    
    return res, count

def longPalindrome(string, maxLength): 
    st = 0
    length = len(string) 
  
    low = 0
    high = 0 
    for i in range(1, length): 
        low = i - 1
        high = i 
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
  
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1 
  
    return maxLength

#string = 'nayannamantenet'
string = 'aaaaa'
#string = 'aaaabaaaa'
n = len(string)
maxlength = 1
maxlength = longPalindrome(string, maxlength)
if maxlength==len(string):
        print(string[0])
        print(string[1:len(string)-1])
        print(string[len(string)-1])
        
else:
    l = round(n/3)
    for i in range(0,n,l):
        res, count = checkPalindrome(i, i+l, string)
        if not count:
            for i in res:
                print(i, end='')
        print()
