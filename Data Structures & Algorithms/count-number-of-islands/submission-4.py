class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ## DFS solution ##
        #Handle empty grid
        if not grid:
            return None

        #Initiate visited and other variables
        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        #DFS
        def dfs(row, col):
            if (0 <= row < rows and 0 <= col < cols) and (row, col) not in visited and grid[row][col] == "1":
                visited.add((row, col))
                
                dfs(row-1, col)
                dfs(row+1, col)
                dfs(row, col-1)
                dfs(row, col+1)

            return None


        #Iterate
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    islands += 1

        return islands