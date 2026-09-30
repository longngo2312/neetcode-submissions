class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set() 
        q = deque() 
        rows, cols = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: 
                    q.append((i,j))
                    visited.add((i,j))
        
        time = 0
        while q: 
            for i in range(len(q)):
                r,c = q.popleft()
                direction = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in direction: 
                    nr, nc = r + dr, c + dc 
                    if (min(nr,nc) < 0 or nr == rows or nc == cols or grid[nr][nc] == -1 or grid[nr][nc] == 0 or (nr,nc) in visited):
                        continue 
                    visited.add((nr,nc))
                    q.append((nr,nc))
                    grid[nr][nc] = time + 1
            time += 1

        print(grid)