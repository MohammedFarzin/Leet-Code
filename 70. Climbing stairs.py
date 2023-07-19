def climb_stairs(n):
    a, b = 0 , 1
    for i in range(n):
        a , b = b, a+b
    return b

r_value = climb_stairs(5)
print(r_value)