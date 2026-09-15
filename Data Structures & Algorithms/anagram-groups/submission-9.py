class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs: 
            characterCount = [0] * 26 #there are 26 characters in the alphabet a -> z
            for char in word:
                characterCount[ord(char) - ord("a")] += 1 
            
            result[tuple(characterCount)].append(word)
        
        return list(result.values())