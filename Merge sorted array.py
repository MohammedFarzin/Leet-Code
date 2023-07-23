def merge(num1, num2):
    n = len(num2)
    m = len(num1) - n

    a = m - 1
    b = n - 1
    c = m + n - 1

    while a >= 0 and b >= 0:
        if num1[a] > num2[b]:
            num1[c] = num1[a]
            a -= 1
        else:
            num1[c] = num2[b]
            b -= 1
        c -= 1
    
    if b >= 0:
        num1[:c+1] = num2[:b+1]
    
    print(num1)



merge([4,5,6,0,0,0], [1,2,3])