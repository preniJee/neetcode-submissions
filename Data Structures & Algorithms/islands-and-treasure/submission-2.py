from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        INF = 2147483647

        q = deque()

        # Step 1: Add all treasure cells (0s) to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        # Step 2: BFS from all 0s simultaneously
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Valid empty room (INF)
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == INF
                ):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
