n,l,d = map(int, input().split())
time = []

for i in range(n):

    for j in range(l):
        time.append(0)

    for k in range(5):
        time.append(1)

for m in range(d):
    time.append(1)

index = 1
while True:

    if time[index*d] == 1:
        print(index*d)
        break
    index += 1