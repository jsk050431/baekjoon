from collections import deque
import sys
input = sys.stdin.readline

for i in range(int(input())):
    x, y, numCabbage = map(int, input().split())
    location = [[0]*x for _ in range(y)]

    for j in range(numCabbage):
        loc_x, loc_y = map(int, input().split())
        location[loc_y][loc_x] = 1

    warmsNum = 00
    for loc_y in range(len(location)):
        for loc_x in range(len(location[loc_y])):

            if location[loc_y][loc_x] == 1:
                warmsNum += 1
                dq = deque([[loc_x, loc_y]])

                while dq:
                    _x, _y = dq[-1]
                    location[_y][_x] = 0

                    if _y != 0 and location[_y-1][_x] == 1:
                        dq.append((_x, _y-1))
                    elif _y != y-1 and location[_y+1][_x] == 1:
                        dq.append((_x, _y+1))
                    elif _x != 0 and location[_y][_x-1] == 1:
                        dq.append((_x-1, _y))
                    elif _x != x-1 and location[_y][_x+1] == 1:
                        dq.append((_x+1, _y))
                    else:
                        dq.pop()
    print(warmsNum)