from collections import deque
import sys
input = sys.stdin.readline

nodes = int(input())
pairs = int(input())
graph = [[] for i in range(nodes+1)]

for i in range(pairs):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

dq = deque([1])
visited = set([1])
while dq:
    head = dq.popleft()
    for i in graph[head]:
        if not(i in visited):
            dq.append(i)
            visited.add(i)

print(len(visited)-1)