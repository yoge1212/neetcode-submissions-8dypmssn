class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        visited = set()
        minutes = 0

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            nonlocal minutes
            q = collections.deque()
            q.append((r, c))

            while q:
                current = q.popleft()
                row = current[0]
                col = current[1]

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                infected = False
                for dRow, dCol in directions:
                    newRow = row + dRow
                    newCol = col + dCol

                    if (0 <= newRow < rows) and (0 <= newCol < cols) and grid[newRow][newCol] == 1 and (newRow, newCol) not in visited:
                        visited.add((newRow, newCol))
                        grid[newRow][newCol] = 2
                        q.append((newRow, newCol))
                        infected = True
                
                if infected:
                    minutes += 1





        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    bfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return minutes
        