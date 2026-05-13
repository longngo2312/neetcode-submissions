class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = [[] for _ in range(len(nums)+1)]
        _map = {}

        for index, value in enumerate(nums):
            _map[value] = _map.get(value,0) + 1

        for key, value in _map.items():
            frequency_map[value].append(key)
        ans = []
        for freq in range(len(frequency_map) -1, 0,-1):
            print(frequency_map[freq])
            if len(frequency_map[freq]) != 0: 
                for num in frequency_map[freq]:
                    ans.append(num)
                    if len(ans) == k:
                        return ans
            else:
                continue
        return []
