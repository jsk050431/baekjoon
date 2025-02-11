import sys
input = sys.stdin.readline

for i in range(int(input())):
    length = [0,1,1,1,2,2,3,4,5,7]

    num = int(input())
    if num > 9:
        for j in range(10, num+1):
            length.append(length[j-1] + length[j-5])
            
    print(length[num])