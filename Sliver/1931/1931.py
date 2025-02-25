import sys
input = sys.stdin.readline
N = int(input())

time = []
for i in range(N):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x:(x[1], x[0]))

endtime = time[0][1]
count = 1
for i in range(1,N):
    starttime = time[i][0]
    if endtime <= starttime:
        endtime = time[i][1]
        count += 1

print(count)