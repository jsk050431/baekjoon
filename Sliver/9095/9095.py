import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    list = [0,1,2,4]
    num = int(input())

    for j in range(4, num+1):
        list.append(list[j-3] + list[j-2] + list[j-1])
        
    print(list[num])