class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: 
            return ""
        windowMap = {}
        frequencyT = Counter(t)

        res, lengthWindow = [-1,-1], len(s) + 1 #store indices of the shortest substring

        have, need = 0, len(frequencyT)
        l = 0 
        for r in range(len(s)):
            windowMap[s[r]] = windowMap.get(s[r], 0) + 1
            if s[r] in frequencyT and windowMap[s[r]] == frequencyT[s[r]]:
                have += 1
            
            while have == need: 
                windowMap[s[l]] = windowMap.get(s[l],0) - 1
                if (r - l + 1) <= lengthWindow:
                    res = [l,r]
                    lengthWindow = r - l + 1
                if s[l] in frequencyT and windowMap[s[l]] < frequencyT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res 
        return s[l:r + 1] if (r - l + 1) <= len(s) + 1 else ""

