class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        r = len(s1)
        while r < len(s2) + 1:
            print(s2[l:r])
            if "".join(sorted(s2[l:r])) == "".join(sorted(s1)):
                return True 
            r += 1
            l += 1
        return False 