class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c): 
            rows, cols = len(grid), len(grid[0])
            if min(r,c) < 0 or r == rows or c == cols or grid[r][c] == '0':
                return 
            grid[r][c] = '0'
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1) 
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0': 
                    continue
                else:  
                    res += 1
                    dfs(grid, i, j)
        print(grid)
        return res 