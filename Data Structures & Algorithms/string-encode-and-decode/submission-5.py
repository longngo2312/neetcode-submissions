class Solution:
    def encode(self, strs: List[str]) -> str:
        #initialize encoded string
        encoded = ""
        for s in strs:
            #delimeter between each word will be the length of the word and a #
            encoded += str(len(s)) + "#" + s
        return encoded 
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        #set "i" iteration to be zero and loop through the len of string
        while i < len(s):
            #Set up "j" as a finder for #
            j = i
            #while s[j] couldn't find # keep incrementing j index 
            while s[j] != "#":
                j += 1 
            #length will be the value number from the encoded string from position i to j (when s[j] found #)
            length = int(s[i:j])
            #append the word from s[j+1] (first letter of the word after #) to s[j+1+length] (the entire word after the first letter so j will end up at the next number value of the next word)
            res.append(s[j+1 : j+1+length])
            #increase the iteration to j so that i doesn't have to loop through every single character in the string
            i = j + 1 + length  
        return res 
        #TC: O(n)
        #SC: O(n+m)