import sys
from collections import deque

while True:
    deq = deque()
    arr = sys.stdin.readline()

    if arr == '.\n':
        break

    yes = True
    for i in arr:

        if i=='(' or i=='[':
            deq.appendleft(i)
        
        if i==')':
            if len(deq)!=0 and deq[0]=='(':
                deq.popleft()
            else:
                yes = False
                break

        if i==']':
            if len(deq)!=0 and deq[0]=='[':
                deq.popleft()
            else:
                yes = False
                break
    
    if yes and len(deq)==0:
        print('yes')
    else:
        print('no')