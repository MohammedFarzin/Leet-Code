def isPalindrome(x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        half = 0
        while x > half:
            half = half * 10 + x % 10
            x = x // 10
        print(half)
        return x == half or half // 10 == x


print(isPalindrome(12321))


