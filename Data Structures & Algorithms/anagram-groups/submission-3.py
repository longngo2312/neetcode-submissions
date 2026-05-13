class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for word in strs:
            count = [0] * 26 #because there are 26 letters in the alphabet
            for char in word:
                count[ord(char)-ord("a")] += 1
            maps[tuple(count)].append(word)

        return list(maps.values())