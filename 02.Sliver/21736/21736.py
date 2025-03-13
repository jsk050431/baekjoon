from collections import deque
import sys
input = sys.stdin.readline

lenY, lenX = map(int, input().split())
graph = []
visited = set()

for i in range(lenY):
    graph.append([j for j in input().strip()])

def startpos():
    for _y in range(lenY):
        for _x in range(lenX):
            if graph[_y][_x] == 'I':
                return (_x,_y)
            
dq = deque([startpos()])
count = 0
while dq:
    _x, _y = dq.popleft()

    if graph[_y][_x] == 'P':
        count += 1

    dis = [(-1,0),(1,0),(0,-1),(0,1)]
    for nextdis in dis:
        next_x = _x + nextdis[0]
        next_y = _y + nextdis[1]

        if not((next_x, next_y) in visited) and 0 <= next_x <= lenX-1 and 0 <= next_y <= lenY-1 and graph[next_y][next_x] != 'X':
            visited.add((next_x, next_y))
            dq.append((next_x, next_y))

if count == 0:
    print("TT")
else:
    print(count)