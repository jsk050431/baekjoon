n = int(input())
list = [0,1]

if n == 1:
    print(1)
else:
    for i in range(2, n+1):
        list.append(list[i-2]+list[i-1])
    print(list[-1])