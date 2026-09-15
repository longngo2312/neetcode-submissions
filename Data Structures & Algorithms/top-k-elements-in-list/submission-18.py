class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)

        bucket = [[] for i in range(len(nums)+1)]
        for key, value in frequency.items():
            bucket[value].append(key)
        
        res = []
        for i in range(len(bucket) - 1, -1,-1):
            for element in bucket[i]:
                res.append(element)
                if len(res) == k:
                    return res 
        
