nums =[3,3,4]

elements = set(nums)
num_count = {}
for i in elements:
    num_count[i] = 0

for i in range(len(nums)):
    num_count[nums[i]] += 1


max = 0
for i in num_count:
    if num_count[i] > max:
        max = num_count[i]
        max_element = i
print(max_element)