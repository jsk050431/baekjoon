nums = input().split('-')

for i in range(len(nums)):
    nums[i] = sum(map(int, nums[i].split('+')))

print(nums[0] - sum(nums[1:]))