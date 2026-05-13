class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += str(len(word)) + "#" + word
        print(string)
        return string
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0       
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j
        print(ans)
        return ans
