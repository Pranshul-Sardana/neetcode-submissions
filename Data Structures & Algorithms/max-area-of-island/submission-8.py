class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ## DFS solution ##

        #Handle empty grid
        if not grid:
            return 0

        #Initiate visited
        visited = set()
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        #Implement DFS
        def dfs(row, col):
            
            if (row < 0 or row == rows or col < 0 or col == cols) or (row, col) in visited or grid[row][col] == 0:
                return 0

            visited.add((row, col))

            return (1 + dfs(row-1, col) + dfs(row+1, col) + dfs(row, col-1) + dfs(row, col+1))


        #Iterate
        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, dfs(row, col))

        return max_area