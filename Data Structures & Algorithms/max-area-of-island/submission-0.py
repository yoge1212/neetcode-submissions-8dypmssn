class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #perform bfds on every node that is a 1
        # as we go through the bfs evey time we add a node to the queue
        #we increase the island area counter by 1
        #at the end of bfs we compare the currentmax island area to the current bfs island area

        if not grid:
            return 0

        visited = set()
        maxIslands = 0
        hasIsland = False

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            nonlocal maxIslands
            q = collections.deque()
            q.append((r, c))
            area = 0

            while q:
                current = q.popleft()
                area += 1
                row = current[0]
                col = current[1]

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dirRow, dirCol in directions:
                    newRow = row + dirRow
                    newCol = col + dirCol

                    if (0 <= newRow < rows) and (0 <= newCol < cols) and grid[newRow][newCol] == 1 and (newRow, newCol) not in visited:
                        visited.add((newRow, newCol))
                        q.append((newRow, newCol))
            maxIslands = max(maxIslands, area)
                    


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    visited.add((r, c))
                    bfs(r, c)
                    hasIsland = True



        if hasIsland:
            return maxIslands
        else:
            return 0

        
        