class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Handle empty grid
        if not grid:
            return None

        #Initiate visited and other variables
        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        #BFS
        def bfs(row, col):
            q = deque()
            q.append([row, col])
            visited.add((row, col))

            while q:
                row, col = q.popleft()

                directions = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]

                for row, col in directions:
                    if (0 <= row < rows and 0 <= col < cols) and (row, col) not in visited and grid[row][col] == "1":
                        q.append([row, col])
                        visited.add((row, col))

            return None


        #Iterate
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands