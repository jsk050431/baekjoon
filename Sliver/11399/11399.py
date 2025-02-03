n = int(input())
time = sorted(list(map(int, input().split())))
totaltime = [time[0]]

for i in range(n-1):
    totaltime.append(totaltime[i]+time[i+1])

print(sum(totaltime))