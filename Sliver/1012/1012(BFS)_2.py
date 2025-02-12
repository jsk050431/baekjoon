from collections import deque
import sys
input = sys.stdin.readline

def firstTarget(list):
    for _y in range(len(list)):
        for _x in range(len(list[_y])):
            if list[_y][_x] == 1:
                return (_x,_y)
    return -1

testRepeat = int(input())
for i in range(testRepeat):
    x, y, numCabbage = map(int, input().split())

    location = [[0]*x for _ in range(y)]
    graph = [[[] for _ in range(x)] for _ in range(y)]

    for j in range(numCabbage):
        loc_x, loc_y = map(int, input().split())
        location[loc_y][loc_x] = 1

    warmsNum = 0
    while True:
        target = firstTarget(location)

        if target == -1:
            break 
        else:
            warmsNum += 1
            dq = deque([target])
            location[target[1]][target[0]] = 0
            while dq:
                _x, _y = dq.popleft()

                near = []
                if _y != 0 and location[_y-1][_x] == 1:
                    near.append((_x, _y-1))
                if _y != y-1 and location[_y+1][_x] == 1:
                    near.append((_x, _y+1))
                if _x != 0 and location[_y][_x-1] == 1:
                    near.append((_x-1, _y))
                if _x != x-1 and location[_y][_x+1] == 1:
                    near.append((_x+1, _y))

                for k in near:
                    if location[k[1]][k[0]] == 1:
                        location[k[1]][k[0]] = 0
                        dq.append(k)
    print(warmsNum)

