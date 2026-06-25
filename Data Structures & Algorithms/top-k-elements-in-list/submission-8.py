class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = [[] for i in range(len(nums) + 1)]
        print(frequencyMap)
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        print(count)
        for item in count:
            print(count[item])
            frequencyMap[count[item]].append(item)
        res = []
        for i in range(len(frequencyMap) - 1, -1, -1):
            if k > 0:
                for num in frequencyMap[i]:
                    res.append(num)
                    k -= 1
            if k == 0:
                return res 
        return []