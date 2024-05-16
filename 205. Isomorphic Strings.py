from collections import Counter

def isIsomorphic(s: str, t: str) -> bool:
    map1 = []
    map2 = []

    for idx in s:
        map1.append(s.index(idx))
    
    for idx in t:
        map2.append(t.index(idx))

    if map1 == map2:
        return True
    return False

def isIsomorphic1(s: str, t: str) -> bool:
    zipped_set = set(zip(s, t))
    return len(zipped_set) == len(set(s)) == len(set(t))

a="paper"
b="title"
print(isIsomorphic1(a, b))