import sys
input = sys.stdin.readline
len_y, len_x, havingBlocks = map(int, input().split())

ground = []
sumByHight = [0]*257
for i in range(len_y):
    inputNum = list(map(int, input().split()))
    ground.extend(inputNum)
    for j in inputNum:
        sumByHight[j] += 1

minHight = min(ground)
maxHight = max(ground)
for i in range(maxHight-1, minHight-1, -1):
    sumByHight[i] += sumByHight[i+1]

timeList = []
for setHight in range(minHight, maxHight+1):
    time = 0
    needBlocks = 0
    getBlocks = 0

    for checkHight in range(minHight, maxHight+1):
        if checkHight <= setHight:
            blockNum = len(ground) - sumByHight[checkHight]
            needBlocks += blockNum
            time += blockNum
        if checkHight > setHight:
            blockNum = sumByHight[checkHight]
            getBlocks += blockNum
            time += 2*blockNum

    if havingBlocks + getBlocks >= needBlocks:
        timeList.append([time, setHight])

timeList.sort(key=lambda x:(x[0], -x[1]))
print(*timeList[0])