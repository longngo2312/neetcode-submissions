class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map = {}
        for num in nums:
            counter_map[num] = counter_map.get(num,0) + 1
        print(counter_map)
        res = []

        _map = [[] for _ in range((len(nums) + 1))]
        print(_map)
        for key,value in counter_map.items():
            _map[value].append(key)
        
        print(_map)
        for i in range(len(_map) - 1, 0, -1):
            for num in _map[i]:
                if k > 0:
                    res.append(num)
                    k -= 1
                if k == 0:
                    return res
        print(res) 
        return [] 
        
