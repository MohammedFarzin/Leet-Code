import re
def palindarom(s):
        s = re.sub("[^A-Za-z0-9]", "", s.lower())
        print(s[::-1])
        print(s)
        if s == s[::-1]:
            return True
        return False

print(palindarom("0P"))