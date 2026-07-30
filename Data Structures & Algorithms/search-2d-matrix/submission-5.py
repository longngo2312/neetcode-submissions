class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #O(log(m*n))
        #idea: Pretend that the matrix is a sorted 1D arrays
        #find row by // len(rows) cols by % len(cols)
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m*n - 1
        while l <= r:
            mid = (l + r) // 2
            rows = mid // n
            cols = mid % n
            num = matrix[rows][cols]
            if num == target:
                return  True 
            elif num < target: 
                l = mid + 1
            else: 
                r = mid - 1
        return False 