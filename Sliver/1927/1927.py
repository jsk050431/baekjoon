import sys
input = sys.stdin.readline

heap = []

def swap(x,y):
    global heap
    temp = heap[x]
    heap[x] = heap[y]
    heap[y] = temp

def pop():
    global heap
    if len(heap) == 0:
        print(0)
    else:
        print(heap[0])
        heap[0] = heap[-1]
        del heap[-1]
        index = 0
        while True:
            if 2*index+1 > len(heap)-1:
                break
            
            if 2*index+2 > len(heap)-1 or heap[2*index+1] <= heap[2*index+2]:
                nextIndex = 2*index+1
            else:
                nextIndex = 2*index+2
            
            if heap[index] <= heap[nextIndex]:
                break
            else:
                swap(index, nextIndex)
                index = nextIndex

def push(num):
    global heap
    heap.append(num)
    index = len(heap)-1
    while True:
        if index == 0:
            break
        
        nextIndex = (index-1)//2
        if heap[index] < heap[nextIndex]:
            swap(index, nextIndex)
            index = nextIndex
        else:
            break

if __name__ == '__main__':
    for repeat in range(int(input())):
        inputNum = int(input())
        if inputNum == 0:
            pop()
        else:
            push(inputNum)