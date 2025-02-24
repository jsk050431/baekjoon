n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr)))
dic = {}

for i in range(len(arr2)):
    dic[arr2[i]] = i
    
print(*list(map(lambda x: dic[x], arr)))