class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                current = q.popleft()
                row = current[0]
                col = current[1]
                direcitons = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in direcitons:
                    if ((row + dr) in range(rows) and (col + dc) in range(cols) 
                    and grid[row+dr][col+dc] == "1" and (row + dr, col + dc) not in visited):
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))

                
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands

        