class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        r = len(s1)

        map1 = {}
        for char in s1:
            map1[char] = map1.get(char, 0) + 1
        
        while r < len(s2) + 1:
            map2 = {}
            for char in s2[l:r]:
                map2[char] = map2.get(char,0) + 1
            if map1 == map2:
                return True 
            r += 1
            l += 1
        return False 