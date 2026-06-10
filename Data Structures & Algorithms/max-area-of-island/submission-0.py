from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        if not grid:
            return max_area
        
        n_rows, n_cols = len(grid), len(grid[0])

        visited = set()

        directions = [(1,0),(-1,0), (0,1), (0,-1)]
        # return the islan area
        def find_island(r,c):
            q = deque()
            q.append((r,c))

            island_area = 1
            
            while q :
                r,c = q.pop()

                for dr, dc in directions:
                    adj_r , adj_c = r + dr, c + dc
                    if  ((adj_r in range(n_rows)) and (adj_c in range(n_cols)) and
                        grid[adj_r][adj_c] == 1 and
                        (adj_r,adj_c) not in visited):

                        visited.add((adj_r,adj_c))
                        q.append((adj_r,adj_c))

                        island_area += 1
            
            return island_area                

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    visited.add((r,c))
                    island_area = find_island(r,c)
                    max_area = max(max_area, island_area)

        return max_area
