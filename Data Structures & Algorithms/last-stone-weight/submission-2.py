class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        heap = stones 

        while len(heap) > 1: 
            val1, val2 = heapq.heappop_max(heap), heapq.heappop_max(heap) 

            heapq.heappush_max(heap, abs(val1-val2))
        
        return heap[0]