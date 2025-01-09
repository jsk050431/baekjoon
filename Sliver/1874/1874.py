import sys
from collections import deque

n = int(input())
stack = deque()
numlist = deque(range(n,0,-1))
printout = []

def push():
    stack.appendleft(numlist.pop())
    printout.append('+')

def pop():
    stack.popleft()
    printout.append('-')


no = False
for i in range(n):
    num = int(sys.stdin.readline())
    
    if i == 0:
        for j in range(num):
            push()
        pop()
    
    elif len(stack) == 0 or stack[0] < num:
        while len(stack) == 0 or stack[0] != num:
            push()
        pop()

    elif stack[0] == num:
        pop()
     
    else:
        print('NO')
        no = True
        break

if not(no):
    for k in printout:
        print(k)