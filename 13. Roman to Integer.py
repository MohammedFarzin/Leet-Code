s = "MCMXCIV"

rom_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
sum = 0
for i in range(len(s)):
    if i < len(s)-1 and rom_to_int[s[i]] < rom_to_int[s[i+1]]:
        sum -= rom_to_int[s[i]]
    else:
        sum += rom_to_int[s[i]]

print(sum)