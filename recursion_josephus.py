def josephus(n, k):
    
    ll = []
    i=1
    while i<=n:
        ll.append(i)
        i+=1
        
    i=1
    while len(ll)!=1:
        index = (i+k)%n
        ll.pop(index)
        i+=1
    return ll

def main():
    T= int(input())

    while(T>0):
        nk = [int(x) for x in input().split()]
        n = nk[0]
        k = nk[1]

        print(josephus(n,k))


if __name__=="__main__":
    main()
