'''
포맷팅
%s -> string
%d -> int
%f -> float
%% -> %
'''

pi = 3.1415926535
print('%0.2f%%' %pi) # 3.14%
#-----------------------------------

a = [1,2,3]
print(a) # [1,2,3]
print(*a) # 1,2,3

# -----------------------------------

#딕셔너리
a = {} # a = dict() 와 동일

a[1] = 'a' # 1->key, 'a'->value
# a = {1:'a'} 

'''
a.keys() -> 모든 key
a.values() -> 모든 value
a.items() -> 모든 key와 value를 함께
'''

#응용
b = {'a': 1, 'b': 2}
print(sum(b.values())) # 3