import sys
input = sys.stdin.readline

nodes = int(input())
pairs = int(input())
graph = {}
visited = set()

def DFS(n):
    visited.add(n)
    for i in graph[n]:
        if not(i in visited):
            DFS(i)


if nodes == 1:
    print(0)

else:
    for i in range(pairs):
        a,b = map(int, input().split())

        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]

    DFS(1)
    print(len(visited)-1)