from collections import deque
import sys
input = sys.stdin.readline

node, edge, start = map(int, input().split())
graph = [[] for i in range(node+1)]
visited = set([start])

def DFS(n):
    print(n, end=" ")
    for i in sorted(graph[n]):
        if not(i in visited):
            visited.add(i)
            DFS(i)

for i in range(edge):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

DFS(start)
print()

visited = set([start])
dq = deque([start])
while dq:
    head = dq.popleft()
    print(head, end=" ")
    for i in sorted(graph[head]):
        if not(i in visited):
            visited.add(i)
            dq.append(i)
