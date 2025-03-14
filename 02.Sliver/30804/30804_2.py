number = int(input())
arr = list(map(int, input().split()))
lenMax = 0

start = 0
end = 0
types = [0]*10
types[arr[0]] += 1
typecount = 1

while end < len(arr):    
    if typecount <= 2:
        end += 1
        if end < len(arr):
            if types[arr[end]] == 0:
                typecount += 1
            types[arr[end]] += 1
    else:
        lenMax = max(lenMax, end-start)
        types[arr[start]] -= 1
        if types[arr[start]] == 0:
            typecount -= 1
        start += 1
lenMax = max(lenMax, end-start)

print(lenMax)