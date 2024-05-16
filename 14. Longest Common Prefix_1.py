strs = ["a","a","b"]
prefix = strs[0]
for i in range(1, len(strs)):
    word = strs[i]
    index = 0
    for j in range(min(len(prefix), len(word))):
        if prefix[j] == word[j]:
            index += 1
            temp = prefix[:index] if index != 0 else ""
        else:
            break
    prefix = temp 28. Find the Index of the First Occurrence in a String


print(prefix)