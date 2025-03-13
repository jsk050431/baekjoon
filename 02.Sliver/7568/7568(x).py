big_list = []
n = int(input())

for i in range(n):
    big_list.append(list(map(int, (input()+' '+str(i+1)+' 0').split())))

big_list.sort(reverse=True)

rank = 1
for j in range(n-1):

    if big_list[j][3] != 0:
        continue

    big_list[j][3] = rank

    temp_rank = rank + 1
    for k in range(j+1, n):
        if big_list[j][1] < big_list[k][1] and big_list[k][3] == 0:
            big_list[k][3] = rank
            temp_rank += 1

    rank = temp_rank

big_list[n-1][3] = rank
# big_list.sort(key=lambda x: x[2])

for l in big_list:
    print(l)