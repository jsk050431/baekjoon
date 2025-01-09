import sys
location = []

for i in range(int(input())):
    location.append(list(map(int, sys.stdin.readline().split())))

location.sort(key=lambda x: (x[1], x[0]))

for j in location:
    print(*j)