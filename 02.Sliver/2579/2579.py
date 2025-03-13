import sys
input = sys.stdin.readline

n = int(input())
stairs = [0]*n
score = [int(input()) for _ in range(n)]


def minNext(k):

    if stairs[k] != 0:
        return stairs[k]
    
    elif k == n-3 or k == n-2:
        stairs[k] = score[k]
        return(stairs[k])
    
    elif k == n-4:
        stairs[k] = score[k] + score[k+2]
        return(stairs[k])
    
    else:
        a = minNext(k+2)
        b = minNext(k+3)
        if a < b:
            stairs[k] = score[k] + a
        else:
            stairs[k] = score[k] + b
        return stairs[k]


if n==1 or n==2:
    print(sum(score))

elif n == 3:
    print(sum(score)-min(score))

else:
    passedScore = [minNext(0), minNext(1), minNext(2)]
    print(sum(score)-min(passedScore))