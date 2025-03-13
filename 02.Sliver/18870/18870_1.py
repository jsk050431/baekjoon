n = int(input())
arr = list(map(int, input().split()))
dic = {}

num = 0
for target in sorted(arr):
    if not(target in dic):
        dic[target] = num        
        num += 1

arr = list(map(lambda x: dic[x], arr))
print(*arr)