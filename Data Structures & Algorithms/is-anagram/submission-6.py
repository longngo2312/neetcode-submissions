class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        mapt = {}
        if len(s) != len(t):
            return False 
        for char in range(len(s)):
            maps[s[char]] = 1 + maps.get(s[char], 0)
            mapt[t[char]] = 1 + mapt.get(t[char], 0)
        for value in maps:
            if maps[value] != mapt.get(value,0):
                return False
        return True 