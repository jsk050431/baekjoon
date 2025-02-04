import sys
input = sys.stdin.readline
dict = {}
a,b = map(int, input().split())

for i in range(a):
    site, password = input().split()
    dict[site] = password

for j in range(b):
    print(dict[input().strip()])