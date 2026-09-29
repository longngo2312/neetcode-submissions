class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set() 
        q = deque() 
        time = 0 

        totalFreshFruit = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    totalFreshFruit += 1
                if grid[i][j] == 2: 
                    visited.add((i,j))
                    q.append((i,j))

        if totalFreshFruit == 0: return 0
        while q: 
            for i in range(len(q)):
                r, c = q.popleft() 
                
                # if totalFreshFruit == 0: 
                #     return time 

                direction = [[1,0], [-1,0], [0,1],[0,-1]]
                
                for dr, dc in direction: 
                    nr, nc = r + dr, c + dc

                    if min(nr, nc) < 0 or nr == len(grid) or nc == len(grid[0]) or grid[nr][nc] == 0 or (nr, nc) in visited: 
                        continue

                    visited.add((nr,nc))
                    q.append((nr,nc))
                    totalFreshFruit -= 1
                    if totalFreshFruit == 0: 
                        return time + 1
            time += 1
        
        return -1
         
                     
