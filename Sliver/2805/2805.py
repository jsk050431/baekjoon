treeNum, needHeight = map(int, input().split())
trees = list(map(int, input().split()))
height_set = set()

start = 0
end = max(trees)
while True:
    h_target = (start+end)//2
    getHeight = sum(map(lambda x: x-h_target, list(filter(lambda x: x>h_target, trees))))
    
    if start == end:
        break
    
    elif getHeight < needHeight:
        end = h_target

    elif getHeight >= needHeight:
        start = h_target+1
        height_set.add(h_target)

print(max(height_set))