expression = input()+'+'
nums = []

start = 0
for i in range(len(expression)):
    if expression[i]=='+' or expression[i]=='-':
        end = i
        nums.append(expression[start:end])
        start = i

list = []
for m in range(len(nums)):

    if nums[m][0] == '-' and m+1 != len(nums):
        for n in range(m+1, len(nums)):    

            if n == m+1:
                max = int(nums[n])
                temp = int(nums[n])
                endIndex = n
            else:
                temp += int(nums[n])

            if temp > max:
                max = temp
                endIndex = n

        list.append([m+1, endIndex, max])

list.sort(key=lambda x: x[2], reverse=True)

if len(list) == 0:
    print(sum(map(int,nums)))
else:
    print(sum(map(int,nums))-2*list[0][2])
