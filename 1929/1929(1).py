m,n = map(int, input().split())

for i in range(m,n+1):

    if i == 1:
        continue

    div = 2
    isprime = True
    
    while div**2 <= i:
        if i%div == 0:
            isprime = False
            break
        div += 1

    if isprime:
        print(i)