import sys

def round(n):
    if abs(n-int(n)) >= 0.5:
        if n >= 0:
            return int(n)+1
        else:
            return int(n)-1
    else:
        return int(n)

num = []

for i in range(int(sys.stdin.readline())):
    num.append(int(sys.stdin.readline()))

num.sort()

# 평균
print(round(sum(num)/len(num)))

# 중간값
print(num[len(num)//2])

#최빈값
num_mode_dict = dict()
for j in num:
    if j in num_mode_dict:
        num_mode_dict[j] += 1
    else:
        num_mode_dict[j] = 1

num_mode = []
mode_max = max(num_mode_dict.values())
for k in num_mode_dict:
    if num_mode_dict[k] == mode_max:
        num_mode.append(k) # 위에서 num이 이미 정렬이 되어있으므로 num_mode도 정렬된 순으로 추가됨.

if len(num_mode) != 1:
    print(num_mode[1])
else:
    print(num_mode[0])

#범위
print(max(num)-min(num))