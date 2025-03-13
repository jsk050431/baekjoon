from collections import deque

locFinder, locHider = map(int, input().split())
graph = deque([locFinder])
visited = set()

timeCount = -1
while True:
    timeCount += 1
    for i in range(len(graph)):
        target = graph.popleft()
        
        if target in visited:
            continue
        else:
            visited.add(target)

        if target == locHider:
            print(timeCount)
            exit()
        else:
            graph.extend(filter(lambda x: 0<=x<=100000, [target-1, target+1, target*2]))