class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        bucket = [[] for i in range(len(nums) + 1)]

        for key, value in counter.items():
            bucket[value].append(key)
        
        res = []
        for i in range(len(bucket) - 1, -1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res 
        
        return []