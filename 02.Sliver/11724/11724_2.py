from collections import deque
import sys
input = sys.stdin.readline
node, edge = map(int, input().split())
graph = [[] for _ in range(node+1)]
visited = set()

for i in range(edge):
    nodeA, nodeB = map(int, input().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)

connection = 0
for i in range(1, len(graph)):
    if not(i in visited):
        connection += 1
    if graph[i]:
        dq = deque([i])
        while dq:
            target = dq.popleft()
            if not(target in visited):
                dq.extend(graph[target])
                visited.add(target)
print(connection)