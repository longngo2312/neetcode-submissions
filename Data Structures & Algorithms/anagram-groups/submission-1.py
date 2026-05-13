class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        res = []
        for s in strs:
            char = sorted(s)
            hashmap[tuple(char)].append(s)
        for value in hashmap.values():
            res.append(value)
        return res 
