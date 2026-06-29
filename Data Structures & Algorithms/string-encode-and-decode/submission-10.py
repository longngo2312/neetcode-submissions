class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f"{len(word)}#" + word
        return res
    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0 
        j = 1
        res = []
        while j < len(s):
            print(i) 
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            sliceword = j + 1 + length 
            res.append(s[j+1:sliceword])
            i = sliceword
            j = i + 1
        return res