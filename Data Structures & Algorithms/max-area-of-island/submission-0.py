class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0 
        def dfs(grid, r,c, visited):
            if (min(r,c) < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == 0 or (r,c) in visited):
                return 0

            visited.add((r,c))
            return 1 + dfs(grid, r + 1, c, visited) + dfs(grid, r - 1, c, visited) + dfs(grid, r, c + 1, visited) + dfs(grid, r, c - 1, visited)     
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    value = dfs(grid,i,j, visited)
                    res = max(res, value)

        return res 

