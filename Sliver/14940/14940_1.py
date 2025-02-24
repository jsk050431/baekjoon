# 미완성

from collections import deque
import sys
input = sys.stdin.readline

lenX, lenY = map(int, input().split())
arr = []
distanceArr = [[0]*lenX for _ in range(lenY)]
for i in range(lenY):
    arr.append(list(map(int, input().split())))

for _y in range(lenY):
    for _x in range(lenX):
        dq = deque()
        visited = set()

        if arr[_y][_x] == 0 or arr[_y][_x] == 2:
            pass

        else:
            dq.append((_x, _y))
            distance = 0
            breakloop = 0
            while dq:
                for i in range(len(dq)):
                    loc_x, loc_y = dq.popleft()
                    visited.add((loc_x, loc_y))
                    if arr[loc_y][loc_x] == 2:
                        distanceArr[_y][_x] = distance
                        breakloop = 1
                        break

                    elif distanceArr[loc_y][loc_x] == -1:
                        distanceArr[_y][_x] = -1
                        breakloop = 1
                        break

                    elif distanceArr[loc_y][loc_x] != 0:
                        distanceArr[_y][_x] = distance + distanceArr[loc_y][loc_x]
                        breakloop = 1
                        break

                    else:
                        nextloc = [(-1,0), (1,0), (0,-1), (0,1)]
                        for j in nextloc:
                            next_x = loc_x + j[0]
                            next_y = loc_y + j[1]
                            if  0<=next_x and next_x<=lenX-1 and 0<=next_y and next_y<=lenY-1 and arr[next_y][next_x]!=0 and not((next_x, next_y) in visited):
                                dq.append((next_x, next_y))
                distance += 1
                if breakloop:
                    break
                if not(dq):
                    distanceArr[_y][_x] = -1

for i in distanceArr:
    for j in i:
        print(j, end=' ')
    print()