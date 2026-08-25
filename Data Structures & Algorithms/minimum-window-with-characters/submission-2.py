class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0: return ""

        currentMap, countT = {}, {}
        res, lengthRes = [-1,-1], float("infinity")

        #build countT first 
        for char in t: 
            countT[char] = 1 + countT.get(char,0)
        
        have,need = 0, len(countT)

        l = 0 
        for r in range(len(s)):
            char = s[r]
            #build current map adding one 
            currentMap[char] = 1 + currentMap.get(char,0)

            #if character in countT show up and the frequency on 2 map equals that means we have 1 => update
            if char in countT and currentMap[char] == countT[char]:
                have += 1
            while have == need:
                #updating result 
                if (r - l + 1) < lengthRes:
                    res = [l,r] 
                    lengthRes = r - l + 1

                #closing the window while updating result to get the smallest 
                currentMap[s[l]] -= 1
                if s[l] in countT and currentMap[s[l]] < countT[s[l]]:
                    have -= 1

                l+= 1

        l,r = res 
        return s[l:r+1] if lengthRes != float("infinity") else ""
             
