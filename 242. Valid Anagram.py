s = "anagram"
t = "nagaram"

def is_anagram(s, t):
    sort_s = sorted(s)
    sort_t = sorted(t)
    return sort_s == sort_t


print(is_anagram(s, t))