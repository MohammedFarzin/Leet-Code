from collections import Counter

def min_deletions(s):
    cnt = Counter(s)
    deletions = 0
    used_freq = set()
    
    sorted_freq = sorted(cnt.values(), reverse=True)

    for freq in sorted_freq:
        if freq not in used_freq:
            used_freq.add(freq)
            continue

        while freq > 0 and freq in used_freq:
            freq -= 1
            deletions += 1
        
        used_freq.add(freq)
        
    return deletions