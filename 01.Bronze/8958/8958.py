for i in range(int(input())):
    answer = list(filter(None, input().split('X')))

    score = 0
    for j in answer:
        score += (1+len(j))*len(j)//2
    print(score)