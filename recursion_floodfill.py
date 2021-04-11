#code
wall = -1

def floodfill(x, y, color):
    global target_color, wall, arr

    if x<M and y<N:
        if arr[x][y]== wall or arr[x][y]==color:
            return 0
        if arr[x][y]!= target_color:
            return 0

        arr[x][y] = color
        
    floodfill(x+1, y, color)
    floodfill(x-1, y, color)
    floodfill(x, y+1, color)
    floodfill(x, y-1, color)

test_case = int(input())
for i in range(test_case):
    M, N = list(map(int, input().split())) 
    arr_list = list(map(int, input().split()))
    x, y, color = list(map(int, input().split()))
    arr = []
    k=0
    for i in range(M):
        arr.append([])
        for j in range(N):
            arr[i].append(arr_list[k])
            k+=1
    target_color = arr[x][y]
    floodfill(x, y, color)
    
    for i in range(M):
        for j in range(N):
            print(arr[i][j], end=' ')
    print()
