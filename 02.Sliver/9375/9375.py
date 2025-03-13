import sys
input = sys.stdin.readline

for i in range(int(input())):
    collections = {}

    for j in range(int(input())):
        cloth = input().split()

        if cloth[1] in collections:
            collections[cloth[1]] += 1
        else:
            collections[cloth[1]] = 1

    answer = 1
    for k in collections:
        answer *= collections[k]+1
    print(answer-1)