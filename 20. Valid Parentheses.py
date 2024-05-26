def is_valid(s):
    if len(s) % 2!= 0: return False

    stack = []
    paren = {
        "[":"]",
        "{":"}",
        "(": ")"
    }
    for i in range(len(s)):
        if s[i] in "[{(":
            stack.append(paren[s[i]])
        elif s[i] in "])}" and len(stack) == 0:
            return False
        else:
            val = stack.pop()
            if val != s[i]:
                return False
    return len(stack) == 0

s = "(]"
print(is_valid(s))