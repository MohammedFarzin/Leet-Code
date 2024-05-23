pattern = "abba"
s = "dog cat cat dog"


def word_pattern(str, pattern):
    s = pattern
    t = str.split()
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

print(word_pattern(s, pattern))