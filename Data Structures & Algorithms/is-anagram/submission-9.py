class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if length of two strings are different then they're not anagram
        if len(s) != len(t):
            return False
        
        mapS = {}
        mapT = {}
        
        for char in s:
            mapS[char] = mapS.get(char,0) + 1
        
        for char in t:
            mapT[char] = mapT.get(char,0) + 1
        
        
        return mapS == mapT

        #TC: O(s + t)
        #SC: O (s + t)        
