def summary_ranges(nums):
    ranges, r = [], []
    for n in nums:
        if n-1 not in r:
            r = []
            ranges += r,
        r[1:] = n,
    return [" -> ".join(map(str, r)) for r in ranges]
        

nums = [0,2,3,4,6,8,9]
print(summary_ranges(nums))