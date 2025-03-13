expression = input()+'+'
nums = []

start = 0
for i in range(len(expression)):
    if expression[i]=='+' or expression[i]=='-':
        end = i
        nums.append(expression[start:end])
        start = i

index = None
for i in range(1,len(nums)):
    if index == None and nums[i][0] == '-':
        index = i
    nums[i] = int(nums[i][1:])
nums[0] = int(nums[0])

if index == None:
    print(sum(nums))
else:
    print(sum(nums[:index]) - sum(nums[index:]))