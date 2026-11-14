class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Practice both DFS and BFS way

        # DFS

        # Handle edge case
        if not grid:
            return 0

        # Get rows and cols lengths
        rows, cols = len(grid), len(grid[0])

        # Initate a seen set
        seen = set()

        # Initiate island count
        n = 0

        # implement dfs with recursion
        def dfs(row, col):
            # Handle edge cases 
            if (row not in range(rows) or col not in range(cols) or 
                grid[row][col] == "0" or (row, col) in seen 
                ):
                return

            seen.add((row, col))

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        # Double iterate on matrix shape
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0" or (row, col) in seen:
                    continue
                dfs(row, col)
                n += 1


        # Return count
        return n
