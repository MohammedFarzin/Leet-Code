def length_of_last_word(s):
    n = len(s)
    idx = n - 1
    len_count = 0

    while idx >= 0 and s[idx] == " ":
        idx -= 1
    
    while idx >=0 and s[idx] != " ":
        len_count += 1
        idx -= 1

    return len_count

s = '   fly me   to   the moon  '
r_value = length_of_last_word(s)
print(r_value)