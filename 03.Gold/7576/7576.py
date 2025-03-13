from collections import deque
import sys
input = sys.stdin.readline
lenx, leny = map(int, input().split())
tomatoes = []
for i in range(leny):
    tomatoes.append(list(map(int, input().split())))

dq = deque()
for y in range(leny):
    for x in range(lenx):
        if tomatoes[y][x] == 1:
            dq.append((x,y))

time = -1
while dq:
    for i in range(len(dq)):
        x, y = dq.popleft()
        move = [(-1,0),(1,0),(0,-1),(0,1)]
        for j in move:
            next_x = x + j[0]
            next_y = y + j[1]
            if (0 <= next_x < lenx) and (0 <= next_y < leny) and (tomatoes[next_y][next_x] == 0):
                dq.append((next_x, next_y))
                tomatoes[next_y][next_x] = 1
    time += 1

for i in tomatoes:
    for j in i:
        if j == 0:
            print(-1)
            exit()
print(time)