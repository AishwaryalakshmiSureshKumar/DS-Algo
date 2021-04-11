from queue import Queue

def nonrepChar(arr, n):
    global MAXCHAR
    q = Queue()
    charCount =[0] * MAXCHAR

    for i in range(n):

        q.put(arr[i])

        charCount[ord(arr[i]) - ord('a')]+=1

        while not q.empty():
            if (charCount[ord(q.queue[0]) - ord('a')]>1):
                q.get()
            else:
                print(q.queue[0], end=' ')
                break
        if q.empty():
            print('-1', end=' ')
    print()

        
    

test_case = int(input())
for i in range(test_case):
    elems = int(input())
    arr = list(map(str, input().strip().split()))
    MAXCHAR = 26
    nonrepChar(arr, elems)
