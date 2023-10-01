class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return ' '.join(s)


sl = Solution()
s = "vector<string> split (string s, char delimiter)"
print(sl.reverseWords(s))