N,R,C = map(int, input().split())

def divide(firstN, lastN, _x, _y):
    if firstN+1 == lastN:
        return firstN
    
    else:
        disN = lastN - firstN
        disXY = disN**0.5

        if _y < disXY//2:
            lastN -= disN//2
        else:
            firstN += disN//2
            _y -= disXY//2

        if _x < disXY//2:
            lastN -= disN//4
        else:
            firstN += disN//4
            _x -= disXY//2
        
        return divide(firstN, lastN, _x, _y)

print(divide(0, 2**(2*N), C, R))