class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += f"{len(word)}#" + word #example 5#Hello5#World 
        return string
    def decode(self, s: str) -> List[str]:
        print(s)
        res = [] 
        l = 0 
        r = 1 
        while l < len(s):
            while s[r] != "#":
                r += 1
            
            length = int(s[l:r])
            sliceword = r + 1 + length 
            res.append(s[r+1:sliceword])
            l = sliceword
            r = l + 1 
        return res 
