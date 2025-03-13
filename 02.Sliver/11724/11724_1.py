from collections import deque
import sys
input = sys.stdin.readline
node, edge = map(int, input().split())
graph = [[] for _ in range(node+1)]

for i in range(edge):
    nodeA, nodeB = map(int, input().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)

connection = 0
for i in range(1, len(graph)):
    if graph[i] != 0:
        connection += 1
    if graph[i]:
        dq = deque([i])
        while dq:
            target = dq.popleft()
            if graph[target]:
                for j in graph[target]:
                    dq.append(j)
                graph[target] = 0
print(connection)