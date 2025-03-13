import sys
from collections import deque

for i in range(int(sys.stdin.readline())):

    n, index = map(int, sys.stdin.readline().split())
    deq = deque(list(map(int, sys.stdin.readline().split())))

    order = 0
    while True:

        if deq[0] == max(deq):
            deq.popleft()
            order += 1

            if index == 0:
                print(order)
                break
            else:
                index -= 1
        
        else:
            deq.rotate(-1)
            if index == 0:
                index = len(deq)-1
            else:
                index -= 1