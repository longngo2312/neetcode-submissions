class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for i in range(len(nums) + 1)]
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1
        
        for keys,values in hashMap.items():
            frequency[values].append(keys)
        
        res = [] 
        for i in range(len(frequency) -1, -1,-1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res 
        return res 