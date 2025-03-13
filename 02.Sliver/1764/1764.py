import sys
input = sys.stdin.readline

list = set()
no = []
a,b = map(int, input().split())

for i in range(a):
    list.add(input().strip())

for j in range(b):
    name = input().strip()
    if name in list:
        no.append(name)

no = sorted(no)
print(len(no))
for k in no:
    print(k)