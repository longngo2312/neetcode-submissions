class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {} 

        for string in strs: 
            word = "".join(sorted(string))
            if word not in hashMap:
                hashMap[word] = []
            
            hashMap[word].append(string)
        
        return list(hashMap.values())