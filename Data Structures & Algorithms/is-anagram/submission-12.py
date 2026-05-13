class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        
        mapS = {}
        mapT = {}

        for i in range(len(s)):
            mapS[s[i]] = mapS.get(s[i],0) + 1
        
        for i in range(len(t)):
            mapT[t[i]] = mapT.get(t[i],0) + 1 
        
        return mapS == mapT

       