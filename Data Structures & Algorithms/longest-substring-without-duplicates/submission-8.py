class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        l = 0
        res = 0
        for r in range(0, len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
                print("set after remove: ",hashSet)
            hashSet.add(s[r])
            print("set after add: ", hashSet)
            res = max(res, len(s[l:r + 1]))
        print("final set ", hashSet)
        return res 