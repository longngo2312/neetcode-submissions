class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyArray = [[] for i in range(len(nums) + 1)]
        hashmap = {}
        for num in nums: 
            hashmap[num] = hashmap.get(num, 0) + 1
        print(hashmap)
        print(frequencyArray)
        for keys in hashmap:
            frequencyArray[hashmap[keys]].append(keys)
        
        res = []
        for i in range(len(frequencyArray) - 1, -1, -1):
            for elements in frequencyArray[i]:
                res.append(elements)
                if len(res) == k:
                    return res 
        return res 
