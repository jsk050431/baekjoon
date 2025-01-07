n = list(map(int, input().split()))
dis = set()

for i in range(7):
    dis.add(n[i+1]-n[i])
 
if dis == {1}:
    print('ascending')
elif dis == {-1}:
    print('descending')
else:
    print('mixed')