from collections import defaultdict

def dfsUtil(v, visited, g):

    visited[v]=True
    print(v,)

    for i in g[v]:
        if visited[i]==False:
            dfsUtil(i, visited, g)

def dfs(g, v):
    visited = [False]*v

    for i in range(v):
        if visited[i]==False:
            dfsUtil(i, visited, g)    
        
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        



case = int(input())
for i in range(case):
    v, e = list(map(int, input().split()))
    graphElem = list(map(int, input().split()))
    g = Graph(v)
    for i in range(0, len(graphElem), 2):
        u, v = graphElem[i], graphElem[i+1]
        g.addEdge(u, v)
        g.addEdge(v, u)
    dfs(g, v)



'''2
4 3
0 1 1 2 0 3'''
