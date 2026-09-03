class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        heap = stones 

        while len(heap)> 1:
            val1, val2 = heapq.heappop_max(stones), heapq.heappop_max(stones)
            heapq.heappush_max(stones, abs(val1-val2)) 
        
        return heap[0]