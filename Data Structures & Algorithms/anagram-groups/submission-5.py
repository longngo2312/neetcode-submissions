class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for word in strs:
            if ''.join(sorted(word)) not in hashMap:
                hashMap[''.join(sorted(word))] = []
            hashMap[''.join(sorted(word))].append(word)
        print(hashMap)
        return list(hashMap.values())