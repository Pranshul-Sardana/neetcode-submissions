class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Handle no grid
        if not grid:
            return 0

        #Initiate max_islands, visited, row and cols
        max_area = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        #bfs to get island area
        #Start deque, current area
        #While queue
        #Get directions
        #Look at all 4 directions to get find connected ones
        #Whenever a connected 1 found, increase the current area
        #Compare with island area
        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row, col))

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            area = 1

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    dr, dc = dr + row, dc + col

                    if ((dr, dc) not in visited) and (
                        dr >= 0 and dr < rows and dc >= 0 and dc < cols
                    ) and grid[dr][dc] == 1:
                        #print(dr, dc)
                        area += 1
                        q.append((dr, dc))
                        visited.add((dr, dc))

            return area


        #Iterate
        #If 1 and not visited, apply bfs
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = bfs(row, col)
                    max_area = max(max_area, area)

        return max_area


