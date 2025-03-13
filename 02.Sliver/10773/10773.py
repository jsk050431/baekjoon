import sys
from collections import deque
deq = deque()

for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())

    if num == 0:
        deq.pop()
    else:
        deq.append(num)

print(sum(deq))