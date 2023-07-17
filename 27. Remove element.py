def removeElement(nums, val: int) -> int:
        i = 0
        size = len(nums)
        while i < size:
            if nums[i] == val:
                  nums.pop(i)
                  size -= 1
            else:
                  i += 1
        k = len(nums)
        return k, nums


nums = [0,1, 2, 2, 3, 0, 4, 2]
r_value = removeElement(nums, 2)
print(r_value)