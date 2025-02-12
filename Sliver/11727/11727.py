arr = [0,1,3]
n = int(input())

if n <= 2:
    print(arr[n])
else:
    for i in range(3,n+1):
        arr.append((2*arr[i-2] + arr[i-1])%10007)
    print(arr[n])