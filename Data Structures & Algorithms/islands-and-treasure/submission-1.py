from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])

        if not grid :
            return grid

       
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
      
        # bfs on inf node to find the fshortest path to a cell == 0
        def bfs(row,col):
            q = deque()
            q.append((row,col))

            visited = set()
            visited.add((row,col))

            shortest_path = 0
            while q:
                for i in range(len(q)): 
                    r,c = q.popleft() 

                    for dr,dc in directions:
                        new_r , new_c = r + dr , c + dc
                        if (new_r in range(ROWS) and 
                        new_c in range(COLS) and (new_r,new_c) not in visited 
                        and  grid[new_r][new_c]!= -1): 

                            visited.add((new_r,new_c))

                            if grid[new_r][new_c] == 0 :
                                shortest_path += 1 
                                grid[row][col] = shortest_path
                                return 
                            
                            
                            q.append((new_r,new_c))

                shortest_path += 1
                        # elif grid[new_r][new_c] != -1 :
                        #     shortest_path = grid[new_r][new_c] + 1
                        #     grid[row][col] = shortest_path
                        #     return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2147483647 :
                    bfs(r,c)
     


        

        