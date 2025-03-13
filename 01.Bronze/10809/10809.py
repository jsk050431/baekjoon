str = input()
for i in range(26):
    if chr(65+i) in str:
        print(str.find(chr(65+i)), end=' ')
    else:
        print(-1, end=' ')