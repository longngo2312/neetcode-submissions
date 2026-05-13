class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1  
        res = []
        while l < r:
            summ = numbers[r] + numbers[l]
            print(summ)
            if summ > target:
                r -= 1 
                summ = 0
                continue
            elif summ < target:
                l += 1
                summ = 0
                continue
            else:
                res.append(l + 1)
                res.append(r + 1)
            l += 1
            r -= 1
        return res 
