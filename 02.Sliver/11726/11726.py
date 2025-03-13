arr = [0,1,2,3]
n = int(input())

if n <= 3:
    print(arr[n])
else:
    for i in range(4,n+1):
        arr.append((arr[i-2] + arr[i-1])%10007)
    print(arr[n])