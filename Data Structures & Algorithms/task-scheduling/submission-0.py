class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1
        
        heap = list(counter.values())
        heapq.heapify_max(heap)

        queue = deque()
        time = 0 

        while heap or queue: #if either of those still have values that means there's task to process
            time += 1 
            if heap:
                val = heapq.heappop_max(heap) - 1
                if val != 0:
                    queue.append([val,time + n])
            if queue and queue[0][1] == time:
                heapq.heappush_max(heap, queue.popleft()[0])
                
        
        return time 
