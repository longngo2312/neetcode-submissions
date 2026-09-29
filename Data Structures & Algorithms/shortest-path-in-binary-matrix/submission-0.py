class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set() 
        visited.add((0,0))
        q = deque()
        q.append((0,0))
        length = 0
        direction = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]

        if grid[0][0] == 1:
            return -1

        while q: 
            for i in range(len(q)):
                r,c = q.popleft() 
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return length + 1
                
                for dr, dc in direction: 
                    if min(r + dr, c + dc) < 0 or r + dr == len(grid) or c + dc == len(grid[0]) or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visited: 
                        continue 
                    
                    visited.add((r + dr, c + dc))
                    q.append((r + dr, c + dc))
            length += 1
        
        return -1