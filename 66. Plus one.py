digits = [9]

def plus_one(digits):
    if digits[-1]  < 9:
            digits[-1] += 1
            return digits
    elif len(digits) == 1 and digits[0] == 9:
        return [1, 0]
    else:
        digits[-1] = 0
        digits[0:-1]= plus_one(digits[0:-1])
        return digits

r_value = plus_one(digits)
print(r_value)