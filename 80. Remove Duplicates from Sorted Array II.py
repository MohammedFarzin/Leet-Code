def remove_duplicated(nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i

nums = [0,0,1,1,1,1,2,3,3]
print(remove_duplicated(nums))