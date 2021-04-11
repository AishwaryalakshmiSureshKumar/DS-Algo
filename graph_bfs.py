from collections import defaultdict

def bfs(g, v):
    visited = [False]*v

    queue = list()
    queue.append(0)

    while queue:

        s= queue.pop(0)
        print(s,)

        for i in g[s]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
    


case = int(input())
for i in range(case):
    v, e =list(map(int, input().split()))
    graphElem = list(map(int, input().split()))
    g= Graph(v)
    for i in range(0, len(graphElem), 2):
        u, v = graphElem[i], graphElem[i+1]
        g.addEdge(u, v)
    bfs(g, v)



'''2
5 4
0 1 0 2 0 3 2 4
3 2
0 1 0 2'''
