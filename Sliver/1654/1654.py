import sys
input = sys.stdin.readline
k,n = map(int, input().split())
line = []
for i in range(k):
    line.append(int(input()))

startNum = 1
endNum = max(line)
length_max = 0

while True:
    length = (startNum + endNum)//2
    pcs = sum(map(lambda x: x//length, line))

    # print('start: {}\nend: {}\npcs: {}\nlength: {}\nlength_max: {}\n\n'.format(startNum, endNum, pcs, length, length_max))

    if startNum == endNum:
        if pcs >= n and length > length_max:
            print(length_max+1)
        else:
            print(length_max)
        break

    elif pcs >= n:
        length_max = length
        startNum = length + 1

    elif pcs < n:
        endNum = length