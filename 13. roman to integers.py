def roman_to_integer1(s: str):
    roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    integer = 0
    char = 0
    for char in range(0, len(s)-1):
        if roman[s[char]] < roman[s[char+1]]:
            integer -= roman[s[char]]
        else:
            integer += roman[s[char]]
    print(integer)
    return integer + roman[s[-1]]

roman_to_integer1('MCMXCIV')