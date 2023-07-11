def remove_duplicate(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    return j + 1, nums


value = remove_duplicate(nums=[0,0,1,1,1,2,2,3,3,4])
print(value)