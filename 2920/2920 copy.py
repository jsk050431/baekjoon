n = list(map(int, input().split()))

dis = set(map(lambda x: n[x+1]-n[x], range(7)))
 
if dis == {1}:
    print('ascending')
elif dis == {-1}:
    print('descending')
else:
    print('mixed')