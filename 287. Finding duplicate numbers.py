def sort(nums):
    nums = sorted(nums)
    i = 0
    while i <= len(nums):
        if nums[i] == nums[i+1]:
            return nums[i]
        else:
            i += 1

a = [1, 3, 4, 2, 2]
print(sort(a))