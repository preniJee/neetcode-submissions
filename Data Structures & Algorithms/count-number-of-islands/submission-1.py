
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 
        n_rows = len(grid)
        n_cols = len(grid[0])
        visited = set()
        n_islands = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            
            while q : 
                row, col = q.pop()

                for dr,dc in directions:  
                    r,c = row + dr , col + dc
                    if r in range(n_rows) and c in range(n_cols) and grid[r][c] == "1" and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))


        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    n_islands += 1
        return n_islands



