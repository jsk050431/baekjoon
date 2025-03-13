import sys

def round(n):
    if n-int(n) >= 0.5:
        return int(n)+1
    else:
        return int(n)

def set_diff():
    dif = []
    n = int(sys.stdin.readline())

    if n == 0:
        return 0

    for i in range(n):
        dif.append(int(sys.stdin.readline()))

    discard = round(n*15/100)
    dif.sort()
    del(dif[n-discard : n])
    del(dif[0 : discard])

    return round(sum(dif)/len(dif))

print(set_diff())