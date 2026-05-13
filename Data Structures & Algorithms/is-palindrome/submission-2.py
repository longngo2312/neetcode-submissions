class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = "".join(c for c in s if c.isalnum())
        print(cleanS)
        l, r = 0, len(cleanS) - 1
        while l < r:
            print(cleanS[r].lower(), cleanS[l].lower())
            if cleanS[r].lower() != cleanS[l].lower():
                return False 
            l += 1
            r -= 1

        return True