def search_insert_position_1(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

nums = [1, 3, 5, 6]
target = 7
r_value = search_insert_position_1(nums, target)
print(r_value)


