class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxRate = max(piles)
        res = 0
        l, r = 1, maxRate
        while l <= r:
            print("left, right", l, r)
            mid = (l + r) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / mid)
                print(hour)
            print("rate: ",mid,"hour:",hour)
            if hour <= h:
                res = mid
                r = mid - 1
            elif hour > h: 
                l = mid + 1
        
        return res 