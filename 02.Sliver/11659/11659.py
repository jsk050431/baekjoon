import sys
input = sys.stdin.readline

n_arr, n_test = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = [arr[0]]

for i in range(1, n_arr):
    arr_sum.append(arr_sum[i-1]+arr[i])
arr_sum.append(0)

for i in range(n_test):
    start, end = map(int, input().split())
    print(arr_sum[end-1] - arr_sum[start-2])