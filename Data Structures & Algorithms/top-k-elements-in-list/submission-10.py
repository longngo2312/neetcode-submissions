class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyList = {}
        counter = [[] for i in range(len(nums) + 1)]

        #count the frequency 
        for num in nums: 
            lookUp = frequencyList.get(num,0)
            frequencyList[num] = lookUp + 1
        
        for keys, values in frequencyList.items():
            counter[values].append(keys)
        
        res = []
        for i in range(len(counter) -1, -1,-1):
            for num in counter[i]:
                res.append(num)
                if len(res) == k:
                    return res