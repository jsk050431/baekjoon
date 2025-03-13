biglist = []
compare = None
n = int(input())

for i in range(n):
    biglist.append(list(map(int, (input()+' 0').split())))

for j in range(n):
    compare = biglist[j]
    del(biglist[j])

    rank = 1
    for k in biglist:
        if compare[0] < k[0] and compare[1] < k[1]:
            rank += 1
    compare[2] = rank
    biglist.insert(j, compare)
    compare = None

for m in biglist:
    print(m[2], end=' ')