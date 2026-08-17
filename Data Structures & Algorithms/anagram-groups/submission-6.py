class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort each word then we can build a hashMap from the strs list 
        hashMap = {}
        for word in strs:
            if "".join(sorted(word)) not in hashMap:
                hashMap["".join(sorted(word))] = []
            hashMap["".join(sorted(word))].append(word)
        
        return list(hashMap.values())