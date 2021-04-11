#code in Python2

def longest_palindrome(s):
    length = len(s)
    low,high =0,0
    maxlength=1
    start=0

    for i in range(1, length):
        low = i
        high = i+1

        while low>=0 and high<length and s[low]==s[high]:
            if high-low+1 >maxlength:
                start = low
                maxlength = high-low+1
            low-=1
            high+=1

        low=i-1
        high=i+1

        while low>=0 and high<length and s[low]==s[high]:
            if high-low+1 >maxlength:
                start = low
                maxlength = high-low+1
            low-=1
            high+=1

        return(s[start:start+maxlength])

test_case = int(input())
for i in range(test_case):
    string = input()
    print(longest_palindrome(string))
