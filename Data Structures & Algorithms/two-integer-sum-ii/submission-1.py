class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow = 0
        fast = len(numbers) - 1
         
        res = []
        while slow < fast:
            total = numbers[slow] + numbers[fast]
            if total < target:
                print(total)
                slow += 1
                total = 0 
                continue 
                 
            elif total > target:
                print(total)
                fast -=1
                total = 0
                continue
            else:
                res.append(slow + 1)
                res.append(fast + 1)
            slow += 1
            fast -= 1
        return res 
                 
