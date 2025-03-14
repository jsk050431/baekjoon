number = int(input())
arr = list(map(int, input().split()))
countarr = set()

start = 0
end = 1
types = [0]*10
types[arr[0]] += 1
typecount = 1

while end != len(arr):    
    if typecount <= 2:
        types[arr[end]] += 1
        end += 1
    else:
        countarr.add(end-start-1)
        types[arr[start]] -= 1
        start += 1
    typecount = len(list(filter(lambda x: x>0, types)))

while typecount > 2 and start != len(arr):
    types[arr[start]] -= 1
    typecount = len(list(filter(lambda x: x>0, types)))
    start += 1
countarr.add(end-start)

print(max(countarr))