import sys
input = sys.stdin.readline

nodes = int(input())
pairs = int(input())
graph = [[] for i in range(nodes+1)]
visited = set()

def DFS(n):
    visited.add(n)
    for i in graph[n]:
        if not(i in visited):
            DFS(i)

for i in range(pairs):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

DFS(1)
print(len(visited)-1)