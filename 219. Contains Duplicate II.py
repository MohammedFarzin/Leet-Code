nums = [0,1,2,3,4,0,0,7,8,9,10,11,12,0]
k = 1


def contain_duplicate(nums, k):
    seen = {}

    for i, j in enumerate(nums):
        if j in seen and i - seen[j] <= k:
            return True
        seen[j] = i
    return False
        
print(contain_duplicate(nums, k))