list = []
for i in range(9):
    list.append(int(input()))

dis = sum(list)-100
end = 0

for j in range(0,8):

    for k in range(j+1,9):

        if list[j] + list[k] == dis:
            del(list[j])
            del(list[k-1])
            end = 1
            break

    if end == 1:
        break


list.sort()

for l in list:
    print(l)