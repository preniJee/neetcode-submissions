from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        n_fresh = 0 
        q = deque()

        row_len = len(grid)
        col_len = len(grid[0])

       # count number of fresh and get the rotten ones
        for i in range(row_len): # O(m*n)
            for j in range(col_len):
                if grid[i][j] == 1:
                    n_fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        if n_fresh == 0:
            return 0
        time = 0
        directions = [(0,1), (0,-1) , (1,0), (-1,0)]
        while q :
            length = len(q)
            for i in range(length):
                (row, col) = q.popleft()
                for dr,dc in directions:
                    adj_r, adj_c = row + dr , col + dc
                    if  -1 < adj_r < row_len and -1 < adj_c < col_len and grid[adj_r][adj_c] == 1:
                        grid[adj_r][adj_c] = 2
                        q.append((adj_r, adj_c))
                        n_fresh -= 1
            time += 1
            if n_fresh == 0:
                return time
        
        if n_fresh != 0 :
            return -1

            






            




        