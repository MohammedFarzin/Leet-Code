nums = [3,2,4]
target = 6
value = 0

num_map = {}
n = len(nums)

for i in range(n):
    compelment = target - nums[i]
    if compelment in num_map:
        value =  [num_map[compelment], i]
    num_map[nums[i]] = i

print(value)
