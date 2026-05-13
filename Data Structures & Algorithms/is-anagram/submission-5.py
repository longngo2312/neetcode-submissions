class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Brute force 
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True 
        return False 