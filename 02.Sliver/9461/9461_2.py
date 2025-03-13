import sys
input = sys.stdin.readline

for i in range(int(input())):
    length = [0,1,1,1]

    num = int(input())
    if num > 3:
        for j in range(4, num+1):
            length.append(length[j-2] + length[j-3])
            
    print(length[num])