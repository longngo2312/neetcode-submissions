class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closetPointArr = []

        for point in points:
            x,y = point 

            distance = (0-x)**2 + (0-y)**2
            closetPointArr.append([distance,x,y])
        print(closetPointArr)

        heapq.heapify_max(closetPointArr)

        while len(closetPointArr) > k:
            value = heapq.heappop_max(closetPointArr)
            print("Value POp: ", value)
        for point in closetPointArr:
            point.pop(0)
        
        return closetPointArr
            