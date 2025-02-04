import sys
input = sys.stdin.readline

stairs = []
score = []
n = int(input())

for i in range(n):
    stairs.append(0)

for j in range(n):
    score.append(int(input()))


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
    passedScore = []
    passedScore.append(minNext(0))
    passedScore.append(minNext(1))
    passedScore.append(minNext(2))
    print(sum(score)-min(passedScore))