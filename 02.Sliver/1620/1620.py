import sys
input = sys.stdin.readline
dict = {}
dict2 = {}

n1, n2 = map(int, input().split())
for i in range(n1):
    name = input().strip()
    dict[i+1] = name
    dict2[name] = i+1

for j in range(n2):
    question = input().strip()
    try:
        question = int(question)
        print(dict[question])
    except:
        print(dict2[question])