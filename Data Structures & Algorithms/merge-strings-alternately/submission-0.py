class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 1, 0
        res = word1[0]
        while l < len(word1) and r < len(word2):
                res += word2[r]
                res += word1[l]
                l += 1
                r += 1
        
        if l == len(word1) and r < len(word2):
            res += word2[r:]
        else:
            res += word1[l:]
        return res