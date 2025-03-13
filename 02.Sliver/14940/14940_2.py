from collections import deque
import sys
input = sys.stdin.readline

lenY, lenX = map(int, input().split())
arr = []
distanceArr = [[-1]*lenX for _ in range(lenY)]
for i in range(lenY):
    arr.append(list(map(int, input().split())))

for _y in range(lenY):
    for _x in range(lenX):
        if arr[_y][_x] == 0:
            distanceArr [_y][_x] = 0
        elif arr[_y][_x] == 2:
            start_x, start_y = (_x, _y)
            
dq = deque([(start_x, start_y)])
distance = -1

while dq:
    distance += 1
    for i in range(len(dq)):
        _x, _y = dq.popleft()

        if distanceArr[_y][_x] != -1:
            continue
        else:
            distanceArr[_y][_x] = distance

        nextloc = [(-1,0), (1,0), (0,-1), (0,1)]
        for j in nextloc:
            next_x = _x + j[0]
            next_y = _y + j[1]
            if 0<=next_x<=lenX-1 and 0<=next_y<=lenY-1 and distanceArr[next_y][next_x]==-1:
                dq.append((next_x, next_y))

for i in distanceArr:
    for j in i:
        print(j, end=' ')
    print()