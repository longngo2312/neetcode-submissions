class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {} 

        for string in strs: 
            if "".join(sorted(string)) not in hashMap:
                hashMap["".join(sorted(string))] = []
            
            hashMap["".join(sorted(string))].append(string)
        
        return list(hashMap.values())