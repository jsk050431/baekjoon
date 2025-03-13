import sys
input = sys.stdin.readline

arr = []
white = 0
blue = 0

def check(startIdx_x, endIdx_x, startIdx_y, endIdx_y):
    global arr
    global white
    global blue

    colors = set()
    for i in arr[startIdx_y : endIdx_y]:
        for j in i[startIdx_x : endIdx_x]:
            colors.add(j)

    if len(colors) == 2:
        nextLen = (endIdx_x - startIdx_x)//2
        check(startIdx_x, endIdx_x - nextLen, startIdx_y, endIdx_y - nextLen)
        check(startIdx_x + nextLen, endIdx_x, startIdx_y, endIdx_y - nextLen)
        check(startIdx_x, endIdx_x - nextLen, startIdx_y + nextLen, endIdx_y)
        check(startIdx_x + nextLen, endIdx_x, startIdx_y + nextLen, endIdx_y)
        
    else:
        if colors.pop() == 0:
            white += 1
        else:
            blue += 1

if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        arr.append(list(map(int, input().split())))
    check(0,N,0,N)
    print(white)
    print(blue)