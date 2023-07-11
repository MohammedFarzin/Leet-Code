def first_occurence_in_string(haystack: str, needle: str):
    if len(haystack) < len(needle):
        return -1
    for i in range(len(haystack)):
        j = 0
        k = i
        count = 0
        while j < len(needle):
            if k < len(haystack):
                if needle[j] == haystack[k]:
                    j += 1
                    k += 1
                    count += 1
                    if count == len(needle):
                        return i
                else:
                    break
    return -1
        
haystack = "mississippi"
needle = "issipi"

r_value = first_occurence_in_string(haystack, needle)
print(r_value)
