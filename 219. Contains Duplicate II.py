nums = [1,2,3,1] 
k = 3

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            if abs(i - j ) <= k:
                print("True")
            else:
                print("False")
