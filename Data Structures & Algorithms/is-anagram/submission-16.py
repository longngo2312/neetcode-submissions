class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #optimized using a hashMap to keep track of the character frequencies on each string 
        if len(s) != len(t):
            return False 
        mapS = {}
        mapT = {}

        for char in s:
            mapS[char] = mapS.get(char, 0) + 1
        
        for char in t:
            mapT[char] = mapT.get(char, 0) + 1
        
        print(mapS)
        print(mapT)
        return mapS == mapT