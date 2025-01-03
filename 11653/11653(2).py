n = int(input())

divider = 2
while divider**2 <= n: # 루트n까지만 탐색하면 됨.
    if n % divider == 0:
        n //= divider
        print(divider)
    else:
        divider += 1

if n != 1: # (문제조건: 1일때는 아무것도 출력x)
    print(n) # 단 마지막 자기자신까지 출력해주기.