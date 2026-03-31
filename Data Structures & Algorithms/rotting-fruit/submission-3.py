class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        minutes = 0

        rows = len(grid)
        cols = len(grid[0])


        q = collections.deque()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))


        while q:
            rotted = False
            for _ in range(len(q)):
                current = q.popleft()
                row = current[0]
                col = current[1]

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dRow, dCol in directions:
                    newRow = row + dRow
                    newCol = col + dCol

                    if (0 <= newRow < rows) and (0 <= newCol < cols) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        q.append((newRow, newCol))
                        rotted = True
            if rotted:
                minutes += 1
    



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return minutes
        