class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = Counter(nums)
        heap = []
        for key,val in frequencyMap.items():
            heap.append([val,key])
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        res = []
        for value in heap:
            res.append(value[1])
        return res 