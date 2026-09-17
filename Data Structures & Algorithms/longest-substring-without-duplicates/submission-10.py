class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        appeared = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in appeared: 
                appeared.remove(s[l])
                l += 1

            appeared.add(s[r])
            res = max(res,len(appeared))
        return res