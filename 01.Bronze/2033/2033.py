n = int(input())
length = len(str(n))-1

for i in range(length):
    n = n/10
    if n-int(n) < 0.5:
        n = int(n)
    else:
        n = int(n)+1
print(n * 10**length)