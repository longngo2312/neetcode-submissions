class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        #only adjacent (horizontal or vertical) nodes are allowed to changed color (flood fill). 
        #stop when there's no more adjecent nodes of the original color to update. 
        #repeating the process by checking neighbors 

        def dfs(grid, r, c, visited, original, color):
            ROWS, COLS = len(grid), len(grid[0])
            if min(r,c) < 0 or (r,c) in visited or r == ROWS or c == COLS or grid[r][c] != original: 
                return 
            
            grid[r][c] = color
            
            visited.add((r,c))
            dfs(grid, r + 1, c, visited, original, color)
            dfs(grid, r - 1, c, visited, original, color)
            dfs(grid, r, c + 1, visited, original, color)
            dfs(grid, r, c - 1, visited, original, color)

            visited.remove((r,c))
        
        dfs(image, sr, sc, set(), image[sr][sc], color)

        return image