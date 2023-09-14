def find_median_sorted_arrays(nums1, nums2):
    num = nums1+nums2
    num.sort()
    n = len(num) - 1
    if((n+1) % 2 == 0):
        median = (num[n//2] + num[n//2+1])/2
    else:
        median = (num[(n+1)//2])
    return median

nums1 = [1, 2]
nums2 = [3, 4]
r_value = find_median_sorted_arrays(nums1, nums2)
print(r_value)