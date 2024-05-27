def rotate(nums, k):
    k %= len(nums)
    nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
    print(nums)



nums = [1,2, 3, 4, 5, 6, 7]
k = 3
print(rotate(nums, k))