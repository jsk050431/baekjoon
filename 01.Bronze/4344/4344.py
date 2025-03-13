for i in range(int(input())):
    a = list(map(int, input().split()))
    score_average = sum(a[1:])/a[0]

    count = 0
    for j in a[1:]:

        if j > score_average:
            count += 1
    
    print("%0.3f%%" %(count*100/a[0]))