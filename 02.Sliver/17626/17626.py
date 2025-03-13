num = int(input())
dp = [0]*(num+1)

i = 1
while i**2 <= num:
    dp[i**2] = 1
    i += 1

for j in range(1,num+1):
    if dp[j] == 0:
        temp = dp[j-1]+1
        k = 1
        while k**2 <= j:
            if dp[j-k**2]+1 < temp:
                temp = dp[j-k**2]+1
            k += 1
        dp[j] = temp

print(dp[num])