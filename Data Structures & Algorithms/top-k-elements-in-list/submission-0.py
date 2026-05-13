class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq =[[] for i in range(len(nums)+1)]
        print(freq)
        hashmap = {}
        for num in range(len(nums)):
            hashmap[nums[num]] = 1 + hashmap.get(nums[num],0)
        print(hashmap)
        for n,c in hashmap.items():
            freq[c].append(n)
        print(freq)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 
        