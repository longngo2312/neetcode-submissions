class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointers 
        left = 0 
        right = len(s) -1 
        while left <= right:
            if s[left].isalnum() == False:
                print(s[left])
                left += 1
                continue 
            if s[right].isalnum() == False:
                print(s[right])
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                print(s[left])
                print(s[right])
                return False
            left += 1
            right -= 1 
        return True 
                
            