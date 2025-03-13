import sys
input = sys.stdin.readline
len_y, len_x, havingBlocks = map(int, input().split())

ground = []
for i in range(len_y):
    ground.extend(list(map(int, input().split())))

minHight = min(ground)
maxHight = max(ground)
timeList = []
for setHight in range(minHight, maxHight+1):
    time = 0
    needBlocks = 0
    getBlocks = 0

    for hightHere in ground:
        if hightHere < setHight:
            needBlocks += setHight - hightHere
            time += setHight-hightHere
        elif hightHere > setHight:
            getBlocks += hightHere - setHight
            time += 2*(hightHere-setHight)

    if havingBlocks + getBlocks >= needBlocks:
        timeList.append([time, setHight])

timeList.sort(key=lambda x:(x[0], -x[1]))
print(*timeList[0])