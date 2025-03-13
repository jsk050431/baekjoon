import sys

def round(n):
    if abs(n-int(n)) >= 0.5:
        if n >= 0:
            return int(n)+1
        else:
            return int(n)-1
    else:
        return int(n)

num = []

for i in range(int(sys.stdin.readline())):
    num.append(int(sys.stdin.readline()))

num.sort()

print(round(sum(num)/len(num)))
print(num[len(num)//2])

num_mode = []
for j in range(min(num), max(num)+1):
    num_mode.append([j, num.count(j)])
num_mode.sort(key=lambda x: (-x[1], x[0]))
if  len(num_mode) != 1 and num_mode[0][1] == num_mode[1][1]:
    print(num_mode[1][0])
else:
    print(num_mode[0][0])


print(max(num)-min(num))