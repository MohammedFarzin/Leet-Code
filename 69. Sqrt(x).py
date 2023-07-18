def sqrt(x):
    if x == 0:
        return 0
    
    first, last = 1, x
    while first <= last:
        mid = first + (last - first) // 2
        c  = x // mid
        if mid == x // mid:
            return mid
        elif mid > x // mid:
            last = mid - 1
        else:
            first = mid + 1
    return last


r_value = sqrt(324)
print(r_value)