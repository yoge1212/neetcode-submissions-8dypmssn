class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        gate_coords = deque()
        INF = 2147483647
        def bfs(rooms_queue):
        
            potential_coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            distance = 1
            while rooms_queue:
                
                for i in range(len(rooms_queue)):
                    current = rooms_queue.popleft()
                    row = current[0]
                    col = current[1]

                    for coord_row, coord_col in potential_coords:
                        new_row = row + coord_row
                        new_col = col + coord_col
                        
                        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == INF:
                            grid[new_row][new_col] = distance
                            rooms_queue.append((new_row, new_col))
                            

                
                distance += 1


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    gate_coords.append((row, col))
        bfs(gate_coords)
        