from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        result = []
        for s in strs:
            sorted_s = sorted(s)
            map[tuple(sorted_s)].append(s)

        for value in map.values():
            result.append(value)
    
        return result 
