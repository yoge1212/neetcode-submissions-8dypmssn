class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        visited = set()
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                current = q.popleft()
                r = current[0]
                c = current[1]

                for dirRow, dirCol in directions:
                    row = r + dirRow
                    col = c + dirCol

                    if (0 <= row < rows) and (0 <= col < cols) and grid[row][col] == "1" and (row, col) not in visited:
                        q.append((row,col))
                        visited.add((row, col))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r, c))
                    bfs(r, c)
                    islands += 1
        
        return islands

        