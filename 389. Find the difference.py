class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for char in s + t:
            result ^= ord(char)
        return chr(result)
        
        
s = 'a'
t = 'aa'

sl = Solution()
r_value = sl.findTheDifference(s, t)
print(r_value)
                    