def canConstruct(ransomNote: str, magazine: str) -> bool:
    ran = {}
    mag = {}
    for i in range(len(ransomNote)):
        count = 0
        for j in range(i, len(ransomNote)):
            if ransomNote[i] == ransomNote[j]:
                count += 1
        ran[ransomNote[i]] = count

    for i in range(len(magazine)):
        count = 0
        for j in range(i, len(magazine)):
            if magazine[i] == magazine[j]:
                count += 1
        mag[magazine[i]] = count
    return ran, mag

print(canConstruct(ransomNote="fihjjjjei", magazine="hjibagacbhadfaefdjaeaebgi"))