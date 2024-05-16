needle = "issip"
haystack = "mississippi"
count = 0
for i in range(len(haystack)-len(needle)+1):
    if haystack[i:i+len(needle)] == needle:
        print(i)
        break
    print(-1)    

        