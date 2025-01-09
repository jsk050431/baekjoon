# 이분탐색 사용

n = int(input())
list1 = sorted(list(map(int, input().split())))
m = int(input())
list2 = list(map(int, input().split()))


for i in list2:
    a = 0
    b = n-1

    while True:
        next_index = (a+b)//2

        if list1[next_index] == i:
            print(1, end=' ')
            break

        elif a == b:
            print(0, end=' ')
            break
    
        elif list1[next_index] > i:
            b = next_index

        elif list1[next_index] < i:
            a = next_index + 1