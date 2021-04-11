#code
def repeatedCharr(strr):
    
    h = {}

    for ch in strr:
        if ch in h:
            return ch
        else:
            h[ch] = 0

    return

case = int(input())
for i in range(case):
    strr = str(input())
    print(repeatedCharr(strr))
