class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return "" 

        windowMap, countT = {}, Counter(t) 

        res, lengthRes = [-1,-1], len(s) + 1

        have, need = 0, len(countT)

        l = 0 
        for r in range(len(s)):
            charRight = s[r]
            windowMap[charRight] = windowMap.get(charRight, 0) + 1

            if charRight in countT and windowMap[charRight] == countT[charRight]:
                have += 1
            while have == need:
                charLeft = s[l] 
                windowMap[charLeft] -= 1
                if (r-l+1) < lengthRes:
                    res = [l,r] 
                    lengthRes = (r - l + 1)
                if charLeft in countT and windowMap[charLeft] < countT[charLeft]: 
                    have -= 1
                l += 1
        l,r = res
        return s[l : r + 1] if (r-l+1) < len(s) + 1 else "" 